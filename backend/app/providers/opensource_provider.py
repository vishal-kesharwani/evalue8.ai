import httpx

from app.config import settings
from app.providers.base import LLMProvider


class OpenSourceProvider(LLMProvider):
    """Thin client for the open-source model provider. Final provider choice
    (Together AI vs. Groq vs. self-hosted) is pending — see DECISIONS.md."""

    name = "opensource"

    def __init__(self, base_url: str = "https://api.together.xyz/v1") -> None:
        self._base_url = base_url
        self._api_key = settings.opensource_provider_api_key

    async def generate(self, prompt: str, *, model: str, **kwargs) -> str:
        async with httpx.AsyncClient(base_url=self._base_url) as client:
            response = await client.post(
                "/chat/completions",
                headers={"Authorization": f"Bearer {self._api_key}"},
                json={"model": model, "messages": [{"role": "user", "content": prompt}], **kwargs},
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
