from flask import Flask

def func(x):
    return x + 1


def test_canary():
    assert func(3) == 4