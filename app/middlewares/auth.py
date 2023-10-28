""" src.middlewares.auth """

from flask import g
from flask import request

from app.exceptions import HandlerException
from app.services import AuthService


def authenticator(func):
    """
    Decorator authenticator
    """
    def wrapper(*args, **kwargs):
        try:
            headers = request.headers
            prefix = "Bearer "

            if "authorization" not in headers:
                raise HandlerException(400, "idToken not found")

            token = headers["authorization"]

            if not token.startswith(prefix):
                raise HandlerException(400, "idToken not found")

            if not token[len(prefix) :]:
                raise HandlerException(400, "idToken not found")

            id_token = token[len(prefix) :]

            if not id_token:
                raise HandlerException(400, "idToken not found")

            service = AuthService()
            g.user = service.authentication(id_token)
        except HandlerException as ex:
            ex.abort()
        except Exception as ex:
            HandlerException(500, "Unexpected response: ", str(ex)).abort()

        return func(*args, **kwargs)

    return wrapper
