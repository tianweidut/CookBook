class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) / 2

            cnt = sum([1 for i in nums if i <= mid])
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid

        return low

if __name__ == "__main__":
    s = Solution()
    print s.findDuplicate([2, 1, 1])
    print s.findDuplicate([1, 2, 2])
