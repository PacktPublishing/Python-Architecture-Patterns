from tdd_example import parameter_tdd


def test_negative():
    assert parameter_tdd(-1) == 0


def test_zero():
    assert parameter_tdd(0) == 0


def test_five():
    assert parameter_tdd(5) == 25


def test_seven():
    # Note this test is deliberatly set to fail
    assert parameter_tdd(7) == 0


def test_ten():
    assert parameter_tdd(10) == 100


def test_eleven():
    assert parameter_tdd(11) == 100
