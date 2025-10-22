import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
from lib.my_requests import MyRequests


class TestUserRegistry(BaseCase):
    without_params_create_user = [
        ('username'),
        ('firstName'),
        ('lastName'),
        ('email'),
        ('password')
        ]
    def setup(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
         data = self.prepare_registration()
         response = MyRequests.post('/user/', data=data)
         Assertions.assert_status_code(response, 200)
         Assertions.assert_json_has_key(response, 'id')
         print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration(email)

        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response context {response.content}"


    def test_create_user_with_email_without_commercial_at(self):
        error_email = self.email.replace('@','')
        data = self.prepare_registration(error_email)

        response = MyRequests.post('/user/', data=data)
        #print(response.content)
        #print(response.status_code)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response context {response.content}"

    @pytest.mark.parametrize("without_params_create",  without_params_create_user)
    def test_create_user_without_params(self, without_params_create):
        match without_params_create:
            case 'username':
                data = {
                        'firstName': 'learnqa',
                        'lastName': 'learnqa',
                        'email': self.email,
                        'password': '123'
                }
            case 'firstName':
                data = {
                        'username': 'learnqa',
                        'lastName': 'learnqa',
                        'email': self.email,
                        'password': '123'
                }
            case 'lastName':
                data = {
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'email': self.email,
                        'password': '123'
                }
            case 'email':
                data = {
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'lastName': 'learnqa',
                        'password': '123'
                }
            case 'password':
                data = {
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'lastName': 'learnqa',
                        'email': self.email
                }
            case _:
                assert "Unknown params"
        response = MyRequests.post('/user/', data = data)
        #print(without_params_create)
        #print(response.content)
        #print(response.status_code)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {without_params_create}", \
                f"Unexpected response context {response.content}"

    def test_create_user_with_onesimbol_name(self):
        data = {
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email,
            'password': '123'
        }
        response = MyRequests.post('/user/', data=data)
        #print(response.content)
        #print(response.status_code)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected response context {response.content}"



    def test_create_user_with_large_name(self):
        name = self.generate_random_string(251)
        data = {
            'username': name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email,
            'password': '123'
        }
        response = MyRequests.post('/user/', data=data)
        #print(name)
        #print(response.content)
        #print(response.status_code)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", \
            f"Unexpected response context {response.content}"