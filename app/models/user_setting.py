"""
    Model: UserSettings
"""
from firebase_admin import firestore as _firestore

from app.exceptions import HandlerException
from app.mixins import Record


class UserSettings(Record):
    pass

