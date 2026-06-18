"""LLM Client Wrapper"""

from typing import Optional, List
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class LLMClient:
    """Wrapper for LLM APIs"""

    def __init__(self):
        self.provider = settings.llm_provider
        self._init_provider()

    def _init_provider(self):
        if self.provider == "openai":
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=settings.openai_api_key)
                self.model = settings.openai_model
            except ImportError:
                logger.error("OpenAI client not installed")
                raise
        elif self.provider == "claude":
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
                self.model = settings.anthropic_model
            except ImportError:
                logger.error("Anthropic client not installed")
                raise
        else:
            raise ValueError(f"Unknown LLM provider: {self.provider}")

    def generate(self, prompt: str, temperature: Optional[float] = None, max_tokens: Optional[int] = None) -> str:
        temp = temperature or settings.openai_temperature
        tokens = max_tokens or settings.openai_max_tokens

        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temp,
                    max_tokens=tokens,
                )
                return response.choices[0].message.content
            
            elif self.provider == "claude":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=tokens,
                    temperature=temp,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text
        
        except Exception as e:
            logger.error(f"LLM generation failed: {e}")
            raise

    def chat(self, messages: List[dict], temperature: Optional[float] = None) -> str:
        temp = temperature or settings.openai_temperature

        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temp,
                )
                return response.choices[0].message.content
            
            elif self.provider == "claude":
                response = self.client.messages.create(
                    model=self.model,
                    messages=messages,
                    temperature=temp,
                )
                return response.content[0].text
        
        except Exception as e:
            logger.error(f"Chat failed: {e}")
            raise


llm_client = LLMClient()
