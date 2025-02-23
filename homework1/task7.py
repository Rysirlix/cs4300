import pytest
import numpy as np

def find_mean(nums):
    return np.mean(nums)

def test_find_mean():
    assert find_mean([5,4,3,8]) == 5.0
    assert find_mean([10,10,10,10]) == 10.0

def test_empty():
    with pytest.warns(RuntimeWarning):
        empty = find_mean([])
    assert np.isnan(empty)