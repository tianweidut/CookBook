
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            nsum = numbers[i] + numbers[j]
            if nsum == target:
                break
            elif nsum > target:
                j -= 1
            else:
                i += 1
                
        return [i + 1, j + 1]
