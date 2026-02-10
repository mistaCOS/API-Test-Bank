"""
Базовая модель для всех DTO (Data Transfer Object) в проекте.

Наследуется от Pydantic BaseModel: даёт валидацию полей, сериализацию (model_dump)
и парсинг из JSON. Все модели запросов/ответов API наследуют BaseModel.
"""

from pydantic import BaseModel as BM


class BaseModel(BM):
    """Общая база для моделей API; пока без дополнительных полей."""
    pass
