from main import check_pow2


def test_check_pow2_1():
    assert check_pow2(1024) == True


def test_check_pow2_2():
    assert check_pow2(35) == False
