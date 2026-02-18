from src.main.api.foundation.endpoint import EndPoint
from typing import Dict, Callable, Optional


class HttpRequester:
    def __init__(self, request_spec: Dict[str, str], endpoint: EndPoint, response_spec: Callable):
        self.request_spec = request_spec
        self.endpoint = endpoint
        self.response_spec = response_spec
