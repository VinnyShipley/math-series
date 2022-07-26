from series import fibonacci, lucas, sum_series

#Fibonaccci Tests
def test_fibon_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibon_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibon_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibon_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibon_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibon_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


# Lucas Tests
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


# Sum Tests
def test_sum_fib_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_fib_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sum_lucas_two():
    actual = sum_series(2, 2)
    expected = 3
    assert actual == expected


def test_sum_lucas_three():
    actual = sum_series(3, 2)
    expected = 4
    assert actual == expected

