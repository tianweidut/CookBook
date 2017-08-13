
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        import sys
        min_v = - sys.maxint - 1
        max1 = max2 = max3 = min_v
        
        for n in nums:
            if n in (max1, max2, max3):
                continue
            elif n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
        
        return max1 if max3 == min_v else max3
