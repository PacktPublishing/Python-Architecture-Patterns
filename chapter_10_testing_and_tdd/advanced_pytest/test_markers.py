import pytest
from tdd_example import parameter_tdd


@pytest.mark.edge
def test_negative():
    assert parameter_tdd(-1) == 0


@pytest.mark.edge
def test_zero():
    assert parameter_tdd(0) == 0


def test_five():
    assert parameter_tdd(5) == 25


def test_seven():
    assert parameter_tdd(7) == 49


@pytest.mark.edge
def test_ten():
    assert parameter_tdd(10) == 100


@pytest.mark.edge
def test_eleven():
    assert parameter_tdd(11) == 100
