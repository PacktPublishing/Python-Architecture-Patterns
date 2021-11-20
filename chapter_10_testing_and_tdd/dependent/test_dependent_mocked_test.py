from unittest.mock import patch
from dependent import parameter_dependent


@patch('math.sqrt')
def test_negative(mock_sqrt):
    assert parameter_dependent(-1) == 0
    mock_sqrt.assert_not_called()


@patch('math.sqrt')
def test_zero(mock_sqrt):
    mock_sqrt.return_value = 0
    assert parameter_dependent(0) == 0
    mock_sqrt.assert_called_once_with(0)


@patch('math.sqrt')
def test_twenty_five(mock_sqrt):
    mock_sqrt.return_value = 5
    assert parameter_dependent(25) == 5
    mock_sqrt.assert_called_with(25)


@patch('math.sqrt')
def test_hundred(mock_sqrt):
    mock_sqrt.return_value = 10
    assert parameter_dependent(100) == 10
    mock_sqrt.assert_called_with(100)


@patch('math.sqrt')
def test_hundred_and_one(mock_sqrt):
    assert parameter_dependent(101) == 10
    mock_sqrt.assert_not_called()
