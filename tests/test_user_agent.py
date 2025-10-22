import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAgent(BaseCase):
    params_user_agent = [
        # 1. ============
        (
            'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mobile',
            'No',
            'Android'
        ),
        # 2. ============
        (
            'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
            'Mobile',
            'Chrome',
            'iOS'
        ),
        #3. ============
        (
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Googlebot',
            'Unknown',
            'Unknown'
        ),
        #4. ============
        (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
            'Web',
            'Chrome',
            'No'
        ),
        #5. ============
        (
            'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Mobile',
            'No',
            'iPhone'
        )
    ]
    @pytest.mark.parametrize("user_agent, platform, browser, device",
                             params_user_agent
                             )
    def test_get_user_agent(self, user_agent, platform, browser, device):
        headers = {"User-Agent": user_agent}
        response = MyRequests.get(
            "/user_agent_check",
            headers=headers)
        self.platform = self.get_json_value(response,"platform")
        print("self.platform",self.platform)
        self.browser = self.get_json_value(response, "browser")
        self.device = self.get_json_value(response, "device")

        Assertions.assert_json_value_by_name(
            response,
            "platform",
            platform,
            f"Для {user_agent} получено неожиданное значение. Ожидали '{platform}'."
        )
        Assertions.assert_json_value_by_name(
            response,
            "browser",
            browser,
            f"Для {user_agent} получено неожиданное значение. Ожидали '{browser}'."
        )
        Assertions.assert_json_value_by_name(
            response,
            "device",
            device,
            f"Для {user_agent} получено неожиданное значение. Ожидали '{device}'."
        )