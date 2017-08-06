#coding: utf-8

# a ^ b  = b ^ a
# a ^ 0 = a
# a ^ a = 0
# a ^ b ^ a = b


def swap(n1, n2):
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    return n1, n2

if __name__ == "__main__":
    print swap(10, 15)
