#coding: utf-8

class Meta(type):
    pass

class Complex(metaclass=Meta):
    pass

class FooBar:
    pass


def test():
    foobar = FooBar()
    print(type(foobar))
    print(type(FooBar))  # python3 中FooBar 是type的instance，python2中是object的instance
    print("isinstance(foobar, FooBar)", isinstance(foobar, FooBar))
    print("isinstance(FooBar, Type)", isinstance(FooBar, type))

    print("--" * 10)
    print(type(Complex))


if __name__ == "__main__":
    test()
