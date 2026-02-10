"""
Базовый класс для всех API-запросов (Requester).

Абстрактный класс: хранит заголовки, base_url и функцию проверки ответа (response_spec).
Конкретные реквестеры наследуют Requester и реализуют метод post() для своего эндпоинта.
"""

from abc import ABC, abstractmethod
from typing import Dict, Callable
from src.main.api.models.base_model import BaseModel


class Requester(ABC):
    """Базовый реквестер: инициализация из request_spec (headers, base_url) и response_spec (проверка ответа)."""

    def __init__(self, request_spec: Dict[str, str], response_spec: Callable):
        self.headers = request_spec["headers"]
        self.base_url = request_spec["base_url"]
        self.response_spec = response_spec

    @abstractmethod
    def post(self, model: BaseModel):
        """Отправляет POST-запрос; реализация в наследниках."""
        ...
