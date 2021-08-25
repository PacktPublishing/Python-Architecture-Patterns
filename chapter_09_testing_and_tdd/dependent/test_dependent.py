from dependent import parameter_dependent


def test_negative():
    assert parameter_dependent(-1) == 0


def test_zero():
    assert parameter_dependent(0) == 0


def test_twenty_five():
    assert parameter_dependent(25) == 5


def test_hundred():
    assert parameter_dependent(100) == 10


def test_hundred_and_one():
    assert parameter_dependent(101) == 10
