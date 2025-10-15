# Importing the Pytest library
import pytest


# Creating the common function for input
@pytest.fixture
def input_value():
    input = 8
    return input


@pytest.fixture
def is_adult():
    input = 18
    return input
