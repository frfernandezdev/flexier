"""
    Model: UserRecord
"""
from firebase_admin import auth as _auth

from app.mixins import Record, Auth


class UserRecord(Auth, Record):
    """
    The UserRecord is a small abstraction layer to use firebase-admin auth.

    Args:
        user_record (UserRecord): Instance of UserRecord
        auth (firebase.auth.Client): firebase.auth.Client

    Attribues:
        auth (firebase.auth.Client): Instance of firebase auth client
        uid (str): User uid
        email (str): User email
        email_verified (bool): User verification status
        password (str): User password
        display_name (str): User display_name
        phone_number (str): User phone number
        photo_url (str): User photo_url
        disabled (bool): User status
        provider_data (list):
            uid (str): Provider uid
            display_name (str): User display name
            email (str): User email
            phone_number (str): User phone number
            photo_url (str): User photo url
            provider_id (str): Provider identifier
        custom_claims (dict): Contains session claims
        tokens_valid_after_timestamp (str): token deadline
    """

    def __init__(self, user_record, auth):
        self.auth = auth
        self.uid = user_record.uid
        self.email = user_record.email
        self.email_verified = user_record.email_verified
        self.password = (
            user_record.password if hasattr(user_record, "password") else None
        )
        self.display_name = user_record.display_name
        self.phone_number = user_record.phone_number
        self.photo_url = user_record.photo_url
        self.disabled = user_record.disabled
        self.provider_data = [
            {
                "uid": provider.uid,
                "display_name": provider.display_name,
                "email": provider.email,
                "phone_number": provider.phone_number,
                "photo_url": provider.photo_url,
                "provider_id": provider.provider_id,
            }
            for provider in user_record.provider_data
        ]
        self.custom_claims = user_record.custom_claims
        self.tokens_valid_after_timestamp = user_record.tokens_valid_after_timestamp

