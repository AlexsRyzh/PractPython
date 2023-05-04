import os
from main import binary_search

arr = [1, 2, 3, 4, 5]


def test_binary_search():
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 2) == 1
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) == -1
