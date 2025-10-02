import requests
from lib.base_case import BaseCase


class TestGetMethods(BaseCase):
    def test_get_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response1.text)
        self.some_cookie = self.get_cookie(response1, "HomeWork")
        #assert True,
        #accepted_cookie = "hw_value"
        #assert self.some_cookie == accepted_cookie, f"Accepted cookie {accepted_cookie} is not equal {self.some_cookie}"

    def test_get_header(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response1.headers)
        #assert True
        self.some_header = self.get_header(response1, "x-secret-homework-header")
        #accepted_header = "Some secret value"
        #assert self.some_header == accepted_header, f"Accepted cookie {accepted_header} is not equal {self.some_header}"
