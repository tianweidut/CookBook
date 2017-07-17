
class Solution(object):

    def permute(self, nums):
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
            nums[start], nums[i] = nums[i], nums[start]
            self.dfs(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]


if __name__ == "__main__":
    print Solution().permute([1, 2, 3])
