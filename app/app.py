""" src.api """
import os
import re

from flask import Flask
from flask import jsonify
from flask_cors import CORS

from app.blueprints import auth
from app.helpers import CustomJSONProvider


def create_app():
    """Initialize Application"""
    api = Flask(__name__)

    api.config["JSON_SORT_KEYS"] = False
    api.url_map.strict_slashes = False
    api.json_provider_class = CustomJSONProvider
    api.json = CustomJSONProvider(api)

    CORS(api)

    api.register_blueprint(auth, url_prefix="/auth")

    # Handler Errors HTTP
    def error_handler(err, msg, detail=None):
        return (
            jsonify(
                {
                    "success": False,
                    "err": err,
                    "msg": msg,
                    "detail": str(detail.description),
                }
            ),
            err,
        )

    @api.errorhandler(500)
    def internal_server_error(e):
        return error_handler(500, "Internal server error", e)

    @api.errorhandler(400)
    def bad_request(e):
        return error_handler(400, "Bad request", e)

    @api.errorhandler(401)
    def unauthorized(e):
        return error_handler(401, "Unauthorized", e)

    @api.errorhandler(404)
    def not_found(e):
        return error_handler(404, "Not found endpoint", e)

    return api
