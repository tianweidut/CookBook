# coding: utf-8
from datetime import datetime

def _fib(n, saved_map):
    if n in saved_map:
        return saved_map[n]

    if n <= 1:
        saved_map[n] = n
        return n

    saved_map[n] = _fib(n-1, saved_map) + _fib(n-2, saved_map)
    return saved_map[n]

def fib_bad(n):
    if n <= 1:
        return n
    return fib_bad(n-1) + fib_bad(n-2)

def fib_good(n):
    if n <= 1:
        return (n, 0)

    a, b = fib_good(n-1)
    return a+b, a

def fib(n):
    saved_map = dict()
    return _fib(n, saved_map)

if __name__ == "__main__":
    s = datetime.now()
    for i in range(0, 100):
        print(i, fib(i))
    print(datetime.now() - s)

    s = datetime.now()
    for i in range(0, 100):
        print(i, fib_good(i)[0])
    print(datetime.now() - s)

    s = datetime.now()
    for i in range(0, 30):
        print(i, fib_bad(i))
    print(datetime.now() - s)


