import main


class TestMain:
    def test_print_hi1(self):
        assert main.print_hi("hallo1") == 4

    def test_print_hi2(self):
        assert main.print_hi("hallo2") == 5
