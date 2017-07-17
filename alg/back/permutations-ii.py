
class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) <= 1:
            return [nums]

        self.r = []
        self.dfs(nums, 0)
        return self.r

    def dfs(self, nums, start):
        import copy
        if start == len(nums):
            self.r.append(copy.copy(nums))
            return

        for i in range(start, len(nums)):
            if i != start and (nums[start] == nums[i] or nums[i] in nums[start:i]):
                continue

            nums[start], nums[i] = nums[i], nums[start]
            self.dfs(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]


if __name__ == "__main__":
    print Solution().permuteUnique([1, 2, 3])
    print Solution().permuteUnique([1, 1, 2])
