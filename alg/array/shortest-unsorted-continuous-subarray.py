class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_v = nums[0]
        end = 0
        for i, n in enumerate(nums):
            if n < max_v:
                end = i
            else:
                max_v = n
                
        min_v = nums[-1]
        len_nums = len(nums)
        start = len_nums - 1
        for i, n in enumerate(nums[::-1], 1):
            if n > min_v:
                start = len_nums - i
            else:
                min_v = n
                
        return 0 if end <= start else end - start + 1
