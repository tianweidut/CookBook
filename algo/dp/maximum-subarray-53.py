
class Solution(object):
    def maxSubArray(self, nums):
        import sys
        sum_nums = 0
        max_sum = -sys.maxint

        for n in nums:
            sum_nums += n
            max_sum = max(max_sum, sum_nums)
            if sum_nums < 0:
                sum_nums = 0

        return max_sum


if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
