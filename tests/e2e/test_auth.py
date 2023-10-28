from pytest import fixture
from unittest import TestCase
from wsgi import create_wsgi
from tests.utils import AuthFirebase
    

class Auth(TestCase):
    def setUp(self):
        self.app = create_wsgi().test_client()

        self.auth = AuthFirebase()
        self.auth.login('frfernandezdev@gmail.com', 'tokenizer')
        authorization = self.auth.get_authorization()
        self.app.environ_base['HTTP_AUTHORIZATION'] = f"Bearer {authorization.get('idToken')}"

    def test_current_user(self):
        response = self.app.get('/api/v1/auth')
        
        assert response.status_code == 200
