import requests
from lib.base_case import BaseCase


class TestGetMethods(BaseCase):
    def test_get_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print("Cookies:", response1.cookies)
        self.some_cookie = self.get_cookie(response1, "HomeWork")

    def test_get_header(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        print("Headers:", response1.headers)
        self.some_header = self.get_header(response1, "x-secret-homework-header")
