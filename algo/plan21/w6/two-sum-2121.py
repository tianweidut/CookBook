                                                                                                                                                            class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        
        while i < j:
            c = nums[i] + nums[j]
            if c == target:
                return [nums[i], nums[j]]
            elif c < target:
                i += 1
            else:
                j -= 1
                
        return []