import pytest


@pytest.fixture
def sample_list():
    return [1, 2, 3]


def test_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1, 2, 3, 4]


def test_length(sample_list):
    sample_list.remove(3)
    assert len(sample_list) == 2


'''
Fresh Data for Each Test

With fixture: Each test gets a brand new [1, 2, 3] list
Without fixture: If using shared data, tests can interfere with each other
'''
