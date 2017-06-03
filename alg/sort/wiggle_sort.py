class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        if not nums or len(nums) <= 1:
            return nums

        for i in range(1, len(nums)):
            if i % 2 != 0 and nums[i] < nums[i - 1]:
                self.swap(nums, i, i - 1)
            elif i % 2 == 0 and nums[i] > nums[i - 1]:
                self.swap(nums, i, i - 1)
        return nums

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
