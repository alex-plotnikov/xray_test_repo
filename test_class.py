import pytest


@pytest.mark.xray('XRAY-56')
class TestClass:

    @pytest.mark.xray('XRAY-56')
    def test_one(self):
        x = "this"
        assert 'h' in x

    @pytest.mark.xray('XRAY-56')
    def test_two(self):
        x = "check"
        assert x == 'check'
