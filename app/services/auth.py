""" src.services.auth """
from app.exceptions import HandlerException
from app.firebase import admin_sdk
from app.models import UserRecord


class AuthService:
    """
    Service Auth
    """

    def authentication(self, id_token):
        """
        Authentcation

        Args:
            id_token (str): id token session

        Returns: dict
            uid (str): User uid
            a (UserRecord): UserRecord
            b (User): User
        """

        decoded_token = UserRecord.verify_id_token(
            id_token, check_revoked=True, auth=admin_sdk.auth
        )

        user_record = UserRecord.get_user(decoded_token["uid"], auth=admin_sdk.auth)

        if user_record.disabled:
            raise HandlerException(401, "Account disabled")

        return user_record
