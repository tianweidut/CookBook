class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_n = 0
        # 产生环，所以只需要求环的任意一个起始元素即可
        # 如果没有visited，则最坏情况是相邻元素依次相连，最后O(n) 
        visited = set()
        
        for pos, val in enumerate(nums):
            if pos in visited:
                continue
                
            cnt = 1
            index = pos
            while index != val:
                cnt += 1
                visited.add(val)
                val = nums[val]
            
            max_n = max(max_n, cnt)
        
        return max_n
