""" wsgi """
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app.app import create_app


def create_wsgi():
    """Create wsgi app"""
    wsgi = Flask(__name__)

    # Set api v1.
    wsgi.wsgi_app = DispatcherMiddleware(
        wsgi.wsgi_app, {"/api/v1": create_app().wsgi_app}
    )

    return wsgi
