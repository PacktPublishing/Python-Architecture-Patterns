import pytest


def count_characters(char_to_count, string_to_count):
    number = 0
    for char in string_to_count:
        if char == char_to_count:
            number += 1

    return number


def test_counting():
    assert count_characters('a', 'Barbara Ann') == 3


@pytest.fixture()
def prepare_string():
    # Setup the values to return
    prepared_string = 'Ba, ba, ba, Barbara Ann'

    # Return the value
    yield prepared_string

    # Teardown any value
    del prepared_string


def test_counting_fixture(prepare_string):
    assert count_characters('a', prepare_string) == 6


def test_counting_fixture2(prepare_string):
    assert count_characters('r', prepare_string) == 2
