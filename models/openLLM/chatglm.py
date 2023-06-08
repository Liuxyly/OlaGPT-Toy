from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from typing import Any , List, Mapping, Optional

import json

class ChatGLM(LLM):
  max_token: int = 10000
  temperature: float = 0.1
  top_p: float = 0.9
  history = []
  
  def __init__(self, path_or_repo = "THUDM/chatglm-6b"):
    from transformers import AutoModel, AutoTokenizer
    self.tokenizer = AutoTokenizer.from_pretrained(path_or_repo, trust_remote_code = True, local_files_only=True)
    self.model = AutoModel.from_pretrained(path_or_repo, trust_remote_code = True, local_files_only=True).half().cuda().eval()

  @property
  def _llm_type(self) -> str:
    return "ChatGLM"
  
  def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
    response, history = self.model.chat(self.tokenizer, prompt, history=self.history, max_length=self.max_token, top_p=self.top_p, temperature=self.temperature)
    if stop is not None:
      response = enforce_stop_tokens(response, stop)
    self.history = self.history + [[None, response]]
    return response
