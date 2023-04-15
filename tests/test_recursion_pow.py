from main import recursion_pow


def test_recursion_pow_1():
    assert recursion_pow(12, 2) == 144


def test_recursion_pow_2():
    assert recursion_pow(-3, 0) == 1
