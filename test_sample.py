import pytest


def func(x):
    return x + 1


@pytest.mark.xray('XRAY-56')
def test_answer():
    assert func(4) == 5
