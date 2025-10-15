import pytest


# @pytest.mark.parametrize("value", [1, 2, 3])
# def test_direct(value):
#     assert value > 0

@pytest.fixture
def data(request):
    param = request.param
    return param * 2


@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_indirect(data):
    assert data > 1
