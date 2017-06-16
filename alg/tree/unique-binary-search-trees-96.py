
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp(n)

    def divid_tle(self, start, end):
        if start >= end:
            return 1

        total = 0
        for i in range(start, end + 1):
            left = self.divid(start, i - 1)
            right = self.divid(i + 1, end)
            total += (left * right)

        return total

    def dp(self, n):
        nums = [0] * (n + 1)
        nums[0] = 1
        for i in range(0, n):
            for j in range(0, i + 1):
                nums[i + 1] += nums[j] * nums[i - j]
        return nums[n]

if __name__ == "__main__":
    print Solution().numTrees(3)
    print Solution().numTrees(5)
    print Solution().numTrees(19)
