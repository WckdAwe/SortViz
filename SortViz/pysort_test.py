from .pysort import *

NUMBER_LIST = [5, 3, 8, 2, 1, 7, -3, -12, 4, 9]
SORTED_NUMBER_LIST = [-12, -3, 1, 2, 3, 4, 5, 7, 8, 9]


def test_bubble_sort():
    assert bubble_sort(NUMBER_LIST, None) == SORTED_NUMBER_LIST
