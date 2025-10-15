import pytest


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (1, 0, 1),
    (-1, 4, 3),
])
def test_add_param(a, b, expected):
    print(f"\n{a} + {b} == {expected}")
    assert a + b == expected


'''
Common CLI options:

pytest -q quiet

pytest -v verbose

pytest -k "substring" run tests matching substring

pytest -m "marker" run tests with marker

pytest -x stop after first failure

pytest -s show print output (disable capture)

pytest --maxfail=3 stop after N failures
'''