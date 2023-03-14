import unittest
from ..Euler45 import is_square, is_hexagonal, is_pentagonal


def test_squares():
    assert is_square(4) == True
    assert is_square(9) == True
    assert is_square(15129) == True


def test_non_squares():
    assert is_square(5) == False
    assert is_square(32432) == False
    assert is_square(40753) == False

def test_pentagonal():
    assert is_pentagonal(40755) == True

def test_hexagonal():
    assert is_hexagonal(40755) == True

def test_non_pentagonal():
    assert is_pentagonal(567645) == False

def test_non_hexagonal():
    assert is_hexagonal(567645) == False