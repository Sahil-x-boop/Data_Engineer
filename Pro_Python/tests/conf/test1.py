# Importing the math library
import math


# Creating first test case
def test_check_floor(input_value):
    assert input_value == math.floor(8.34532)


# Creating second test case
def test_check_equal(input_value):
    assert 5 == input_value


def test_age(is_adult):
    assert 24 > is_adult
