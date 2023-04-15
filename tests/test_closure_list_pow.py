from main import closure_list_pow


def test_closure_list_pow_1():
    a = closure_list_pow([1, 2, 3, 4])
    assert a(3) == [1, 8, 27, 64]


def test_closure_list_pow_2():
    a = closure_list_pow([1, 2, 3, 4])
    assert a(2) == [1, 4, 9, 16]


def test_closure_list_pow_3():
    a = closure_list_pow([0, 2, 1, -2])
    assert a(3) == [0, 8, 1, -8]

