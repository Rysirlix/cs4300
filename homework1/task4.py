import pytest

def calculate_discount(price, discount):
    return price - (price * discount / 100)

def test_int_calculate_discount():
    assert calculate_discount(40, 30) == 28

def test_float_calculate_discount():
    assert calculate_discount(59.89, 29.0) == pytest.approx(42.5219)

def test_mixed_calculate_discount():
    assert calculate_discount(30, 17.5) == pytest.approx(24.75)
