"""
Спецификации проверки HTTP-ответов в тестах.

Каждый метод возвращает функцию confirm(response), которую вызывают реквестеры после запроса.
Функция проверяет ожидаемый status_code; при несовпадении тест падает с текстом ответа.
"""

from requests import Response
from http import HTTPStatus


class ResponseSpecs:
    """Статические методы, возвращающие функции проверки кода ответа (для response_spec в Requester)."""

    @staticmethod
    def code_200():
        """Проверяет, что ответ имеет статус 200 OK."""
        def confirm(response: Response):
            return response.status_code == HTTPStatus.OK, response.text
        return confirm

    @staticmethod
    def code_201():
        """Проверяет, что ответ имеет статус 201 Created."""
        def confirm(response: Response):
            return response.status_code == HTTPStatus.CREATED, response.text
        return confirm

    @staticmethod
    def code_400():
        """Проверяет, что ответ имеет статус 400 Bad Request."""
        def confirm(response: Response):
            return response.status_code == HTTPStatus.BAD_REQUEST, response.text
        return confirm

    @staticmethod
    def code_404():
        """Проверяет, что ответ имеет статус 404 Not Found."""
        def confirm(response: Response):
            return response.status_code == HTTPStatus.NOT_FOUND, response.text
        return confirm

    @staticmethod
    def code_422():
        """Проверяет, что ответ имеет статус 422 Unprocessable Entity."""
        def confirm(response: Response):
            return response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, response.text
        return confirm
