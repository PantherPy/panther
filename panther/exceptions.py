from panther import status


class APIException(Exception):
    detail: str | dict | list = 'Internal Server Error'
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail=None, status_code=None):
        self.detail = detail or self.detail
        self.status_code = status_code or self.status_code


class AuthenticationException(APIException):
    detail = 'Authentication Error'
    status_code = status.HTTP_401_UNAUTHORIZED
