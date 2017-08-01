#coding: utf-8
from typing import List

def a(i: int) -> List[int]:
    return [i, i, i]


print(a("fdsfa"))

def t():
    print(a(1))
    print(a(3))
    print(a("fdsfa"))
    print(a.__annotations__)

t()
