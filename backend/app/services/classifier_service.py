import json

from app.providers.base import LLMProvider
from app.schemas.classification import Complexity, Domain, TaskClassification

_CLASSIFICATION_PROMPT = """Classify the following task for an LLM routing system.

Task: "{task}"

Respond with ONLY a JSON object (no markdown, no extra text) with exactly these fields:
- "complexity": one of "simple", "moderate", "complex", "production_critical"
- "domain": one of "general", "coding", "legal", "financial", "technical", "research"
- "latency_sensitive": true or false

Guidance:
- "simple": a short, single-step request (e.g. a rewording, a one-line factual answer).
- "moderate": needs some reasoning or synthesis but has limited scope.
- "complex": multi-step reasoning, long-form output, or cross-referencing multiple pieces of information.
- "production_critical": output will be used in a high-stakes context (legal filing, financial \
disclosure, safety-critical decision) where errors carry serious consequences.
- "latency_sensitive": true only if the task implies an interactive, real-time, or user-facing \
context where a slow response is a problem.
"""


class ClassificationError(Exception):
    pass


class TaskClassifierService:
    def __init__(self, provider: LLMProvider):
        self._provider = provider

    async def classify(self, task: str) -> TaskClassification:
        try:
            raw = await self._provider.generate(_CLASSIFICATION_PROMPT.format(task=task))
            data = json.loads(_strip_markdown_fence(raw))
            return TaskClassification(
                complexity=Complexity(data["complexity"]),
                domain=Domain(data["domain"]),
                latency_sensitive=bool(data["latency_sensitive"]),
            )
        except Exception as exc:
            raise ClassificationError(f"Task classification failed: {exc}") from exc


def _strip_markdown_fence(raw: str) -> str:
    """Providers sometimes wrap JSON in ```json fences despite instructions not to."""
    text = raw.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[len("json") :]
    return text.strip()
