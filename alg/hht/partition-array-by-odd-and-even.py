
class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        if not nums:
            return

        p = 0
        i = 0

        while i < len(nums):
            if nums[i] & 1:
                self.swap(nums, p, i)
                p += 1
                i += 1
            else:
                i += 1

    def swap(self, nums, p, i):
        if p == i:
            return

        t = nums[p]
        nums[p] = nums[i]
        nums[i] = t

if __name__ == "__main__":
    s = [1, 2, 3, 4]
    Solution().partitionArray(s)
    print s
