import pytest

from app.providers.base import LLMProvider
from app.schemas.classification import Complexity, Domain
from app.services.classifier_service import ClassificationError, TaskClassifierService


class FakeProvider(LLMProvider):
    name = "fake"

    def __init__(self, response: str):
        self._response = response

    async def generate(self, prompt: str, **kwargs) -> str:
        return self._response


@pytest.mark.asyncio
async def test_classify_parses_plain_json():
    provider = FakeProvider('{"complexity": "complex", "domain": "financial", "latency_sensitive": true}')
    result = await TaskClassifierService(provider).classify("some task")

    assert result.complexity == Complexity.COMPLEX
    assert result.domain == Domain.FINANCIAL
    assert result.latency_sensitive is True


@pytest.mark.asyncio
async def test_classify_strips_markdown_fence():
    provider = FakeProvider(
        '```json\n{"complexity": "simple", "domain": "general", "latency_sensitive": false}\n```'
    )
    result = await TaskClassifierService(provider).classify("some task")

    assert result.complexity == Complexity.SIMPLE
    assert result.domain == Domain.GENERAL
    assert result.latency_sensitive is False


@pytest.mark.asyncio
async def test_classify_raises_classification_error_on_malformed_json():
    provider = FakeProvider("not json at all")

    with pytest.raises(ClassificationError):
        await TaskClassifierService(provider).classify("some task")


@pytest.mark.asyncio
async def test_classify_raises_classification_error_on_invalid_enum_value():
    provider = FakeProvider('{"complexity": "impossible", "domain": "general", "latency_sensitive": false}')

    with pytest.raises(ClassificationError):
        await TaskClassifierService(provider).classify("some task")


@pytest.mark.asyncio
async def test_classify_propagates_provider_failure_as_classification_error():
    class FailingProvider(LLMProvider):
        name = "failing"

        async def generate(self, prompt: str, **kwargs) -> str:
            raise RuntimeError("auth error")

    with pytest.raises(ClassificationError):
        await TaskClassifierService(FailingProvider()).classify("some task")
