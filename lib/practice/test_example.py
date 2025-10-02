class TestExample:
    def test_check_math(self):
        a = 10
        b = 1
        assert a+b == 11

    def test_check_math2(self):
        a = 10
        b = 11
        expected_sum = 11
        assert a + b == expected_sum, f"Сумма значений переменных а и b не равна {expected_sum}"

    def test_check_math3(self):
        a = 10
        b = 12
        expected_sum = 11
        assert a + b == expected_sum, f"Сумма значений переменных а и b не равна {expected_sum}"