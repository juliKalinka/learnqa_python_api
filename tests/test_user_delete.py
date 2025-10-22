import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
class TestUserDelete(BaseCase):
    def test_delete_user_id_2(self):
        user_id=2
        #login
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #delete
        response3 = MyRequests.delete(f"/user/{user_id}",
                                headers={"x-csrf-token": token},
                                cookies={"auth_sid": auth_sid}
                                  )
        Assertions.assert_status_code(response3, 400)

        assert response3.content.decode("utf-8") == '{"error":"Please, do not delete test users with ID 1, 2, 3, 4 or 5."}', \
            f"Unexpected response context {response3.content}"
    def test_delete_user_just_created(self):
        # register
        register_data = self.prepare_registration()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # delete
        response3 = MyRequests.delete(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_status_code(response3, 200)

        # get
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response4.status_code)
        print(response4.content)
        assert response4.text == "User not found", "Wrong deleted. User exists."
    def test_delete_user_with_other_auth(self):
        # register
        register_data = self.prepare_registration()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')


        user_id = self.get_json_value(response1, "id")

        # login
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # delete
        response3 = MyRequests.delete(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_status_code(response3, 400)

        # get
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response4.status_code)
        print(response4.content)
        assert response3.content.decode(
            "utf-8") == '{"error":"Please, do not delete test users with ID 1, 2, 3, 4 or 5."}', \
            f"Unexpected response context {response3.content}"