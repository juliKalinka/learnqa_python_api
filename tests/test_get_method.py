import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestGetMethods(BaseCase):
    def test_get_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        self.some_cookie = self.get_cookie(response1, "HomeWork")
        print(self.some_cookie)
        accepted_cookie = "hw_value"
        assert self.some_cookie == accepted_cookie,f"Accepted cookie {accepted_cookie} is not equal {self.some_cookie}"
