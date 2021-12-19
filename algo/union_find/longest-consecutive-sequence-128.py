#coding: utf-8


class UnionFind(object):
    def __init__(self, n):
        self.nums = [i for i in range(n)]
        self.sz = [1] * n
        self.count = n

    def find(self, index):
        while index != self.nums[index]:
            self.nums[index] = self.nums[self.nums[index]]
            index = self.nums[index]
        return index

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)

        if ri == rj:
            return

        if self.sz[ri] < self.sz[rj]:
            self.sz[rj] += self.sz[ri]
            self.nums[ri] = rj
        else:
            self.sz[ri] += self.sz[rj]
            self.nums[rj] = ri

        self.count -= 1


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_map = {}
        for i, n in enumerate(set(nums)):
            nums_map[n] = i

        uf_pairs = []

        def append_up(n, orig):
            if n in nums_map:
                uf_pairs.append((orig, n))

        for n in nums:
            append_up(n - 1, n)
            append_up(n + 1, n)

        uf = UnionFind(len(nums_map))
        for n, m in uf_pairs:
            uf.union(nums_map[n], nums_map[m])

        return max(uf.sz)


def main():
    s = Solution()
    #print s.longestConsecutive([100, 4, 200, 1, 3, 2])

    s = Solution()
    print s.longestConsecutive([0, 0, -1])

if __name__ == "__main__":
    main()
