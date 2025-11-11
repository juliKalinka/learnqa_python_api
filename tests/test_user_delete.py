import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("Delete user cases")
class TestUserDelete(BaseCase):
    def test_delete_user_id_2(self):
        user_id = 2
        with allure.step(f"Login user with user_id={user_id}"):
            login_data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response2 = MyRequests.post("/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step(f"Try deleted user user_id={user_id}"):
            response3 = MyRequests.delete(f"/user/{user_id}",
                                          headers={"x-csrf-token": token},
                                          cookies={"auth_sid": auth_sid}
                                          )
            Assertions.assert_status_code(response3, 400)
            Assertions.assert_response_content_use_decode(response3,
                                                          '{"error":"Please, do not delete test users with ID 1, 2, '
                                                          '3, 4 or 5."}')

    def test_delete_user_just_created(self):
        with allure.step(f"Register new user"):
            register_data = self.prepare_registration()
            response1 = MyRequests.post("/user/", data=register_data)

            Assertions.assert_status_code(response1, 200)
            Assertions.assert_json_has_key(response1, 'id')

            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step(f"Login created user"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step(f"Try deleted user"):
            response3 = MyRequests.delete(f"/user/{user_id}",
                                          headers={"x-csrf-token": token},
                                          cookies={"auth_sid": auth_sid}
                                          )
            Assertions.assert_status_code(response3, 200)
        with allure.step(f"Try get user"):
            response4 = MyRequests.get(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )
            assert response4.text == "User not found", "Wrong deleted. User exists."

    def test_delete_user_with_other_auth(self):
        with allure.step(f"Register new user"):
            register_data = self.prepare_registration()
            response1 = MyRequests.post("/user/", data=register_data)

            Assertions.assert_status_code(response1, 200)
            Assertions.assert_json_has_key(response1, 'id')
            user_id = self.get_json_value(response1, "id")

        with allure.step(f"Login created user"):
            login_data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response2 = MyRequests.post("/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step(f"Try deleted user"):
            response3 = MyRequests.delete(f"/user/{user_id}",
                                          headers={"x-csrf-token": token},
                                          cookies={"auth_sid": auth_sid}
                                          )
            Assertions.assert_status_code(response3, 400)

        with allure.step(f"Try get user"):
            response4 = MyRequests.get(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )
            Assertions.assert_response_content_use_decode(response4,
                                                          '{"error":"Please, do not delete test users with ID 1, 2, '
                                                          '3, 4 or 5."}')
