""" src.blueprints.auth """
from flask import Blueprint
from flask import g
from flask import jsonify
from flask import request

from app.exceptions import HandlerException
from app.middlewares import authenticator
from app.services import AuthService


router = Blueprint(name="Auth", import_name=__name__)


@router.route("/", methods=["GET"])
@authenticator
def index_auth():
    """
    GET: /api/v1/auth
    """
    return jsonify({"success": True, "response": g.user})


@router.route("/settings", methods=["POST"])
def update_auth_settings():
    pass


@router.route("/settings", methods=["PUT"])
def update_field_auth_settings():
    pass
