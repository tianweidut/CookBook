class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = len(nums)
        r = []
        
        front = [1] * (cnt + 2)
        back = [1] * (cnt + 2)
        
        i = 0
        while i < cnt:
            front[i + 1] = front[i] * nums[i]
            back[cnt - i] = back[cnt + 1 - i] * nums[cnt - 1 - i]
            i += 1
            
        r = []
        for pos, _ in enumerate(nums, 1):
            r.append(front[pos - 1] * back[pos + 1])
        
        return r
            
