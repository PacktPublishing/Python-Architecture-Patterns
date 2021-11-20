import os
import time
import pytest


def count_characters_from_file(char_to_count, file_to_count):
    '''
    Open a file and count the characters in the text contained
    in the file
    '''
    number = 0
    with open(file_to_count) as fp:
        for line in fp:
            for char in line:
                if char == char_to_count:
                    number += 1

    return number


@pytest.fixture()
def prepare_file():
    data = [
        'Ba, ba, ba, Barbara Ann',
        'Ba, ba, ba, Barbara Ann',
        'Barbara Ann',
        'take my hand',
    ]
    filename = f'./test_file_{time.time()}.txt'
    # Setup the values to return
    with open(filename, 'w') as fp:
        for line in data:
            fp.write(line)

    # Return the value
    yield filename

    # Delete the file as teardown
    os.remove(filename)


def test_counting_fixture(prepare_file):
    assert count_characters_from_file('a', prepare_file) == 17


def test_counting_fixture2(prepare_file):
    assert count_characters_from_file('r', prepare_file) == 6
