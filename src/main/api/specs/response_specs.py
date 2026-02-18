from requests import Response
from http import HTTPStatus


class ResponseSpecs:
    @staticmethod
    def code_200():
        def confirm(response: Response):
            return response.status_code == HTTPStatus.OK, response.text
        return confirm

    @staticmethod
    def code_201():
        def confirm(response: Response):
            return response.status_code == HTTPStatus.CREATED, response.text
        return confirm

    @staticmethod
    def code_400():
        def confirm(response: Response):
            return response.status_code == HTTPStatus.BAD_REQUEST, response.text
        return confirm

    @staticmethod
    def code_404():
        def confirm(response: Response):
            return response.status_code == HTTPStatus.NOT_FOUND, response.text
        return confirm

    @staticmethod
    def code_422():
        def confirm(response: Response):
            return response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, response.text
        return confirm
