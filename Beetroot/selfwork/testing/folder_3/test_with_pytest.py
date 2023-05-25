# content of test_sample.py
import pytest
def func(x):
    return x + 1

@pytest.fixture
def test_answer():
    assert func(3) == 5
