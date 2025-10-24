import requests
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestGetMethods(BaseCase):
    def test_get_cookie(self):
        response1 = MyRequests.get("/homework_cookie")
        print("Cookies:", response1.cookies)
        self.some_cookie = self.get_cookie(response1, "HomeWork")

    def test_get_header(self):
        response1 = MyRequests.get("/homework_header")
        print("Headers:", response1.headers)
        self.some_header = self.get_header(response1, "x-secret-homework-header")
