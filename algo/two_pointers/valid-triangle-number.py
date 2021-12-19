class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        if len_n < 3:
            return 0
        
        nums = sorted(nums)
        
        cnt = 0
        i = 0
        while i < len_n - 2:
            if nums[i] == 0:
                i += 1
                continue
                
            k = i + 2    
            j = i + 1
            while j < len_n - 1:
                while k < len_n and nums[k] < nums[i] + nums[j]:
                    k += 1
                cnt += k - j - 1
                j += 1
            
            i += 1
            
        return cnt
        
