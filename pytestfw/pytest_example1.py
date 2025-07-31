# importing the module
import pytest
#defining a function with parameter x
def func(x):
    return x + 5


def test_method2():
    assert func(3) == 8


def test_answer1():
    a = 10
    b = 10
    assert a == b


def test_answer2():
    c = 15
    d = 3 * 5
    assert c == d
