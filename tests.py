import pytest

from defArrays import reverse_array, smallest_and_largest, sum_of_n 
class TestArray:
    def test_def_arrays(self):
        arr = [1, 2, 3, 4, 5]
        assert reverse_array(arr) == [5, 4, 3, 2, 1]
        assert smallest_and_largest(arr) == (1, 5)
        assert sum_of_n(arr) == 15


from sortingTest import insertion_sort, bubble_sort
class TestSorting:
    def test_insertion_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        assert insertion_sort(arr) == [1, 2, 5, 5, 6, 9]

    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]


from searches import linear_search, binary_search
class TestSearches: 
    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5]
        assert linear_search(arr, 3) == 2
    
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 3) == 2