class TestPhrase:

    def test_check_len_15_phrase(self):
        phrase = input("Set a phrase less then 15 simbols: ")
        assert len(phrase) < 15, f"Input phrase '{phrase}' more then 15 simbols or equal"