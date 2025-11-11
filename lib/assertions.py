from requests import Response
import json
import allure
from lib.logger import Logger


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        received_value = response_as_dict[name]
        is_equal = bool(received_value == expected_value)
        Logger.add_results(expected_value, received_value,is_equal)
        with allure.step(f"expected_value '{expected_value}'. \ncurrent_value:{received_value}. \nis_equal: {is_equal}"):
            assert is_equal, f"{error_massage} Received value is equal '{received_value}'"

    @staticmethod
    def assert_response_content_use_decode(response: Response, expected_value):
        current_value = response.content.decode("utf-8")
        is_equal = bool(current_value == expected_value)
        Logger.add_results(expected_value, current_value,is_equal)
        with allure.step(f"expected_value '{expected_value}'. \ncurrent_value:{current_value}. \nis_equal: {is_equal}"):
            assert is_equal, f"Unexpected response context {response.content}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        with allure.step("Check json parsing response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"Response is not in JSON format. Response text is {response.text}"
            for name in names:
                with allure.step(f"Check key {name}"):
                    assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    def assert_json_has_not_keys(response: Response, names: list):
        with allure.step("Check json parsing response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"Response is not in JSON format. Response text is {response.text}"
            for name in names:
                with allure.step(f"Check key {name}"):
                    assert name not in response_as_dict, f"Response JSON have key '{name}'. Which is unacceptable."

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        with allure.step("Check json parsing response"):
            with allure.step(f"Check key {name}"):
                try:
                    response_as_dict = response.json()
                except json.JSONDecodeError:
                    assert False, f"Response is not in JSON format. Response text is {response.text}"
                with allure.step(f"Check present key {name}"):
                    assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        with allure.step(f"Check status_code {expected_status_code}"):
            assert response.status_code == expected_status_code, \
                f"Unexpected status code! Expected:{expected_status_code}. Actual: {response.status_code}"
