"""
Name: test_main.py
Author: itsf4llofstars
Desc: Tests for testing ./src/main.py
"""
from src.functions import add_two_numbers


def test_add_two_numbers_int():
    ans = add_two_numbers(12, 34)
    assert ans == 46


def test_add_two_numbers_flaot():
    ans = add_two_numbers(12.34, 56.78)
    assert ans == 69.12
