import addition_2
import pytest

# Note 1: the two dots (..) means two tests were passed!


def test_add():
    assert addition_2.add(4, 5) == 9


def test_sub():
    assert addition_2.sub(4, 5) == -1
