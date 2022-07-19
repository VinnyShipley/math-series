def fibonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n == 0:
        return 2

    if n == 1:
        return 1

    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, def_one=0, def_two=1):
    if def_one == 0 and def_two == 1:
        return fibonacci(n)

    if def_one == 2 and def_two == 1:
        return lucas(n)
