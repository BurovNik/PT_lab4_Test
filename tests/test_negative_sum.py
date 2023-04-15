from main import negative_sum


def test_negative_sum_1():
    assert negative_sum([1, -2, 3, -5, -3, 14]) == -10


def test_negative_sum_2():
    assert negative_sum([-1, 2, -3, 5, 3, -14]) == -18


def test_negative_sum_3():
    assert negative_sum([1, 2, 3, 5, 3, 14]) == 0



