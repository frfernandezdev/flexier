from requests import Session

BASE_URL = "http://emulator:9099/identitytoolkit.googleapis.com/v1"


class AuthFirebase:
    def __init__(self):
        self.__requests = Session()
        self.__requests.params = {"key": "any"}
        self.__authorization = None

    def get_authorization(self):
        return self.__authorization

    def login(self, email: str, password: str):
        payload = {"email": email, "password": password}
        response = self.__requests.post(
            f"{BASE_URL}/accounts:signInWithPassword", json=payload
        )
        self.__authorization = response.json()
        return response.json()

    def current_user(self):
        if self.__authorization is None:
            raise Exception(
                "Not found authorization data, please check if you have previously executed login"
            )

        payload = {"idToken": self.__authorization.get("idToken")}
        response = self.__requests.post(f"{BASE_URL}/accounts:lookup", json=payload)
        return response.json()

    def create_user(self, email: str, password: str):
        response = self.__requests.post(
            f"{BASE_URL}/accounts:signUp", json={"email": email, "password": password}
        )
        return response.json()

    def update_user(self, email: str, password: str):
        if self.__authorization is None:
            raise Exception(
                "Not found authorization data, please check if you have previously executed login"
            )

        payload = {
            "idToken": self.__authorization.get("idToken"),
            "email": email,
            "password": password,
        }
        response = self.__requests.put(f"{BASE_URL}/accounts:update", json=payload)
        return response.json()

    def delete_user(self):
        if self.__authorization is None:
            raise Exception(
                "Not found authorization data, please check if you have previously executed login"
            )

        payload = {
            "idToken": self.__authorization.get("idToken"),
        }
        response = self.__requests.put(f"{BASE_URL}/accounts:delete", json=payload)
        return response.json()
