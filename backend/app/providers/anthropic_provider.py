from anthropic import AsyncAnthropic

from app.config import settings
from app.providers.base import LLMProvider


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self) -> None:
        self._client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    async def generate(self, prompt: str, *, model: str = "claude-sonnet-5", max_tokens: int = 1024, **kwargs) -> str:
        response = await self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        return response.content[0].text if response.content else ""
