from hypothesis import given, strategies as st
from main import distance


def true_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


@given(x1=st.integers(min_value=10), y1=st.integers(),
       x2=st.integers(), y2=st.integers())
def test_dist(x1, y1, x2, y2):
    assert distance(x1, y1, x2, y2) == true_distance(x1, y1, x2, y2)
