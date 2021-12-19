#coding: utf-8


class Solution(object):
    def findDisappearedNumbers(self, nums):
        if not nums:
            return []

        for i in range(0, len(nums)):
            fi = abs(nums[i]) - 1
            nums[fi] = nums[fi] if nums[fi] < 0 else -1 * nums[fi]

        return [i + 1 for i, n in enumerate(nums) if n > 0]

    def findDisappearedNumbersSpaceN(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        cnt = len(nums)
        all_nums = [0] * (cnt + 1)

        for i in nums:
            all_nums[i] = 1

        return [i for i in range(1, cnt + 1) if all_nums[i] == 0]


if __name__ == "__main__":
    s = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print s
