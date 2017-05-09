#coding: utf-8

#ref: https://www.yunaitong.cn/fenwick-tree.html


class FenwickTree(object):

    def __init__(self, n):
        self.num = [0] * (n + 1)
        self.n = n

    def lowbit(self, x):
        # 补码：按位取反，末尾加1 --> x二进制表示时，从右向左，第一个1保留，其余都置位0时，表示的数字
        return x & (-x)

    def add(self, x, value):
        while x <= self.n:
            self.num[x] += value
            x += self.lowbit(x)

    def sum(self, x):
        r = 0
        while x > 0:
            r += self.num[x]
            x -= self.lowbit(x)

        return r

    def get(self, x):
        r = self.num[x]
        z = x - self.lowbit(x)
        x -= 1

        while x != z and x >= 0:
            r -= self.num[x]
            x -= self.lowbit(x)

        return r


def main():
    i_nums = [2, 4, 5, 7, 9, 10, 15, 22]

    tree = FenwickTree(len(i_nums))
    for i, n in enumerate(i_nums):
        tree.add(i + 1, n)

    print 'tree num store:', tree.num
    print '--' * 10

    print 'tree sum:'
    for i in range(len(i_nums)):
        print i + 1, tree.sum(i + 1)

    print '--' * 10
    print 'check sum'
    total = 0
    for i, n in enumerate(i_nums):
        total += n
        print i + 1, total

    print '--' * 10
    print 'check get'
    for i, n in enumerate(i_nums):
        print n, tree.get(i + 1)

    print tree.get(0)


if __name__ == "__main__":
    main()
