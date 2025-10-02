import requests
import pytest
class TestFirstApi:
    names = [
        ("Vitalii"),
        ("Julia"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self,name):

        url = "https://playground.learnqa.ru/api/hello"
        #name = "Vitalii"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong request code"

        response_dict = response.json()
        assert "answer" in response_dict, "Нет ответа answer в пришедшем ответе"

        if len(name) == 0:
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Пришедший ответ не совпадает с ожидаемым"