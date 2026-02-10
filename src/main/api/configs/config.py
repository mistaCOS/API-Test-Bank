"""
Конфигурация приложения (singleton).

Читает файл resources/urls.properties при первом обращении и хранит пары ключ=значение.
Используется для получения URL бэкенда (backendUrl) и других настроек.
"""

from pathlib import Path
from typing import Any


class Config:
    """Singleton: один экземпляр на всё приложение. При первом создании загружает urls.properties."""

    _isinstance = None
    _dictionary = {}

    def __new__(cls):
        if cls._isinstance is None:
            cls._isinstance = super(Config, cls).__new__(cls)

            # Путь к файлу конфигурации относительно этого модуля
            config_path = Path(__file__).parents[4] / 'resources' / 'urls.properties'

            if not config_path.exists():
                raise FileNotFoundError(f'{config_path} does not exist')

            with open(config_path, 'r') as f:
                for line in f:
                    if "=" in line:
                        key, value = line.split("=")
                        cls._dictionary[key] = value

        return cls._isinstance

    @staticmethod
    def fetch(key: str, default: Any = None) -> Any:
        """Возвращает значение по ключу из конфигурации или default, если ключа нет."""
        return Config()._dictionary.get(key, default)
