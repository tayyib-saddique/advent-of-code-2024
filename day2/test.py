import os, sys
sys.path.append(os.path.abspath('./'))

from part1 import is_gradually_ascending, is_gradually_descending

def test_gradual_increase():
    assert is_gradually_ascending([1, 3, 6, 7, 9]) == True

def test_gradual_decrease():
    assert is_gradually_descending([7, 6, 5, 3, 1]) == True

def test_significant_increase():
    assert is_gradually_ascending([100, 80, 40, 1]) == False

def test_significant_decrease():
    assert is_gradually_descending([1, 30, 50, 90]) == False

def test_alternating():
    assert is_gradually_ascending([1, 3, 6, 5, 3, 1]) == False
    assert is_gradually_descending([1, 3, 6, 5, 3, 1]) == False

def test_duplicates():
    assert is_gradually_ascending([1, 1, 1, 3, 4, 5]) == False
