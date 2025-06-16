import os
import requests

class OpenRouterModel:
    """Simple wrapper for OpenRouter chat completion API."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, model: str, messages: list[dict]) -> str:
        """Send a chat completion request and return the assistant text."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {"model": model, "messages": messages}
        response = requests.post(self.url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
