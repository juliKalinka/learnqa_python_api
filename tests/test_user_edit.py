import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_create_user(self):
        #register
        register_data=self.prepare_registration()
        response1=requests.post("https://playground.learnqa.ru/api/user/",data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1,"id")

        #login
        login_data = {
           'email':email,
           'password':password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #edit
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                headers={"x-csrf-token": token},
                                cookies={"auth_sid": auth_sid},
                                data= {"firstName": new_name}
                                  )
        Assertions.assert_status_code(response3, 200)

        #get
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(response4,
                                             "firstName",
                                             new_name,
                                             "Wrong name the user aftesr edit"
                                             )
    def test_edit_user_without_auth(self):
        #register
        register_data=self.prepare_registration()
        response1=requests.post("https://playground.learnqa.ru/api/user/",data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        user_id = self.get_json_value(response1,"id")
        #edit
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                data= {"firstName": new_name}
                                  )
        Assertions.assert_status_code(response3, 400)
        print(response3.status_code)
        print(response3.content)
        assert response3.content.decode("utf-8") == '{"error":"Auth token not supplied"}', \
            f"Unexpected response context {response3.content}"
    def test_edit_other_user(self):
        # register
        register_data = self.prepare_registration()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # login
        login_data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # edit
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid},
                                     data={"firstName": new_name}
                                     )
        Assertions.assert_status_code(response3, 400)
        #print(response3.status_code)
        #print(response3.content)
        assert response3.content.decode("utf-8") == '{"error":"Please, do not edit test users with ID 1, 2, 3, 4 or 5."}', \
                f"Unexpected response context {response3.content}"

    def test_edit_create_error_email(self):
        #register
        register_data=self.prepare_registration()
        response1=requests.post("https://playground.learnqa.ru/api/user/",data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1,"id")

        #login
        login_data = {
           'email':email,
           'password':password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #edit
        new_email =email.replace('@','')
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                headers={"x-csrf-token": token},
                                cookies={"auth_sid": auth_sid},
                                data= {"email": new_email}
                                  )
        Assertions.assert_status_code(response3, 400)
        assert response3.content.decode("utf-8") == '{"error":"Invalid email format"}', \
                f"Unexpected response context {response3.content}"
    def test_edit_user_short_firstName(self):
        #register
        register_data=self.prepare_registration()
        response1=requests.post("https://playground.learnqa.ru/api/user/",data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1,"id")

        #login
        login_data = {
           'email':email,
           'password':password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #edit
        new_name = self.generate_random_string(1)
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                headers={"x-csrf-token": token},
                                cookies={"auth_sid": auth_sid},
                                data= {"firstName": new_name}
                                  )
        Assertions.assert_status_code(response3, 400)
        assert response3.content.decode("utf-8") == '{"error":"The value for field `firstName` is too short"}', \
            f"Unexpected response context {response3.content}"
