import json.decoder
from requests import Response
from datetime import datetime
import random
import string
import allure

class BaseCase:
    def get_cookie (self, response: Response,cookie_name):
        with allure.step(f"get cookies '{cookie_name}'"):
            assert cookie_name in response.cookies, f"Cannot find cookies with the name {cookie_name} in the last response"
            return response.cookies[cookie_name]
    def get_header (self, response: Response,header_name):
        with allure.step(f"get header '{header_name}'"):
            assert header_name in response.headers, f"Cannot find headers with the name {header_name} in the last response"
            return response.headers[header_name]
    def get_json_value(self, response: Response,name):
        with allure.step("Check json parsing response"):
            try:
                response_as_dict = response.json()
            except json.decoder.JSONDecoderError:
                assert False, f"Response is not JSON Format. Response text is {response.text}"

        with allure.step("Check key in response"):
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration(self, email=None):
        allure.step(f"prepare registration")
        if email is None:
            base_part = 'learnqa'
            domain = 'example.com'
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email,
            'password': '123'
        }

    def generate_random_string(self,length):
        allure.step(f"Generate random string")
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
