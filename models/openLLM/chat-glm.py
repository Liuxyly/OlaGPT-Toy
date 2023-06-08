from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from typing import Any , List, Mapping, Optional

import json

class ChatGLM(LLM):
  max_token: int = 10000
  temperature: float = 0.1
  top_p: float = 0.9
  history = []

  @property
  def _llm_type(self) -> str:
    return "ChatGLM"
  
  def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
    response, history = model.chat(tokenizer, prompt, history=self.history, max_length=self.max_token, top_p=self.top_p, temperature=self.temperature)
    if stop is not None:
      response = enforce_stop_tokens(response, stop)
    self.history = self.history + [[None, response]]
    return response
