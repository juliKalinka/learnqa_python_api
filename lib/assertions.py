from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        received_valie= response_as_dict[name]
        assert received_valie == expected_value, f"{error_massage} Received value is equal '{received_valie}'"

    def assert_get_method(response: Response, _value, expected_value, error_massage):
        assert _value == expected_value, error_massage