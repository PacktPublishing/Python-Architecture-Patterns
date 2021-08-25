import pytest
from unittest.mock import patch
from dependent import parameter_dependent


@patch('math.sqrt')
def test_multiple_returns_mock(mock_sqrt):
    mock_sqrt.side_effect = (5, 10)
    assert parameter_dependent(25) == 5
    assert parameter_dependent(100) == 10


@patch('math.sqrt')
def test_exception_raised_mock(mock_sqrt):
    mock_sqrt.side_effect = ValueError('Error on the external library')
    with pytest.raises(ValueError):
        parameter_dependent(25)
