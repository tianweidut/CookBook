#coding: utf-8


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


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_map = {}
        for i, v in enumerate(sorted(set(nums), reverse=True)):
            num_map[v] = i + 1

        r = []
        cnt = len(num_map)
        tree = FenwickTree(cnt)
        for num in reversed(nums):
            index = num_map[num]
            tree.add(index, 1)
            r.append(tree.sum(cnt) - tree.sum(index))

        return list(reversed(r))


def main():
    test_suits = (
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([5, 2, 1, 6], [2, 1, 0, 0]),
        ([5], [0]),
        ([5], [0]),
        ([26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41],
         [10, 27, 10, 35, 12, 22, 28, 8, 19, 2, 12, 2, 9, 6, 12, 5, 17, 9, 19, 12, 14, 6, 12, 5, 12, 3, 0, 10, 0, 7, 8, 4, 0, 0, 4, 3, 2, 0, 1, 0]),
    )

    for nums, expected_result in test_suits:
        result = Solution().countSmaller(nums)
        print '----'
        print 'e:', expected_result
        print "r:", result
        print result == expected_result


if __name__ == "__main__":
    main()
