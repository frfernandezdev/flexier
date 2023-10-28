"""
    Initialize firebase_admin
"""
from os import getenv
from json import loads

from firebase_admin import auth
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import initialize_app


class sdk:
    def __init__(self, sdk, auth, firestore):
        self.sdk = sdk
        self.auth = auth
        self.firestore = firestore


def initialize_admin():
    _credentials = loads(getenv("FIREBASE_CREDENTIALS"))
    app = initialize_app(credential=credentials.Certificate(_credentials))

    client_auth = auth.Client(app)
    client_firestore = firestore.client(app)

    return sdk(app, client_auth, client_firestore)


admin_sdk = initialize_admin()
