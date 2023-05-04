import pytest
from main import triangle_type


@pytest.fixture
def test1():
    return triangle_type(
        0, 2,
        1, 0,
        -1, 0
    )


@pytest.fixture
def test2():
    return triangle_type(
        0, (12)**0.5,
        -2, 0,
        2, 0
    )


@pytest.fixture
def test3():
    return triangle_type(
        1, 1,
        -2, 0,
        2, 0
    )

##########################################


def test_triangle(test1, test2):
    '''
    x1,y1
    x2,y2
    x3,y3
    '''
    assert test1 == "равнобедренный"

    assert test2 == "равносторонний"


def test_triangle2(test3):
    assert test3 == "разносторонний"


@pytest.mark.parametrize('x1,y1,x2,y2,x3,y3,result', [
    (0, 2, 1, 0, -1, 0, 'равнобедренный'),
    (-10, 20, 0, 10, 20, 10, "разносторонний")
])
def test_triangle3(x1, y1, x2, y2, x3, y3, result):
    assert triangle_type(
        x1, y1,
        x2, y2,
        x3, y3
    ) == result
