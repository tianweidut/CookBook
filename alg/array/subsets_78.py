#coding: utf-8

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import math
        ts = int(math.pow(2, len(nums)))

        r = []
        for i in range(0, ts):
            ri = []
            for n in nums[::-1]:
                if(i & 1 == 1):
                    ri.append(n)
                i = i >> 1

            ri = ri[::-1]
            r.append(ri)

        return r


def main():
    r = Solution().subsets([1, 2, 3])
    print r


if __name__ == "__main__":
    main()
