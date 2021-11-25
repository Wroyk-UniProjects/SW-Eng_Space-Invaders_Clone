import pytest
import main


class TestMain:
    def test_print_hi(self):
        text = "hallo"
        assert main.print_hi(text) == text
