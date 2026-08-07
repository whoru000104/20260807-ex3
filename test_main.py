from main import add, greet


def test_add():
    assert add(1, 2) == 3


def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins!"
