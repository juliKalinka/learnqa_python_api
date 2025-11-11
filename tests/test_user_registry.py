import allure
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
from lib.my_requests import MyRequests


@allure.epic("User registration cases")
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

    @allure.description("This test succssesfully create user")
    def test_create_user_successfully(self):
         data = self.prepare_registration()
         response = MyRequests.post('/user/', data=data)
         Assertions.assert_status_code(response, 200)
         Assertions.assert_json_has_key(response, 'id')

    @allure.description("This test try created user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration(email)

        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        Assertions.assert_response_content_use_decode(response, f"Users with email '{email}' already exists")


    def test_create_user_with_email_without_commercial_at(self):
        error_email = self.email.replace('@','')
        data = self.prepare_registration(error_email)

        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        Assertions.assert_response_content_use_decode(response, f"Invalid email format")

    @allure.description("This test try created user without params")
    @pytest.mark.parametrize("without_params_create",  without_params_create_user)
    def test_create_user_without_params(self, without_params_create):
        with allure.step(f"Set data for request"):
            data = {
                'username': 'learnqa',
                'firstName': 'learnqa',
                'lastName': 'learnqa',
                'email': self.email,
                'password': '123'
            }
        try:
            with allure.step(f"Try deleted data key {without_params_create}"):
                del data[without_params_create]
                response = MyRequests.post('/user/', data = data)
            Assertions.assert_status_code(response, 400)
            Assertions.assert_response_content_use_decode(response,f"The following required params are missed: {without_params_create}")
        except :
            assert False, f"Data don't have key {without_params_create}"

    @allure.description("This test try created user with one simbol name 'l'")
    def test_create_user_with_one_simbol_name(self):
        data = {
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email,
            'password': '123'
        }
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        Assertions.assert_response_content_use_decode(response,
                                                      f"The value of 'username' field is too short")


    @allure.description("This test try created user with large name - 251 random simbols")
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
        Assertions.assert_status_code(response, 400)
        Assertions.assert_response_content_use_decode(response, f"The value of 'username' field is too long")

