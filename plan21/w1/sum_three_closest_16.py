from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        import sys
        nums.sort()

        ans = sys.maxsize
        
        for i in range(0, len(nums)):
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                tmp = nums[i] + nums[start] + nums[end]

                if abs(target - tmp) < abs(target - ans):
                    ans = tmp

                if target == tmp:
                    return target
                elif target > tmp:
                    start += 1
                else:
                    end -= 1

        return ans
                    
                   
if __name__ == "__main__":
	print(Solution().threeSumClosest([-1,2,1,-4], 1))
	print(Solution().threeSumClosest([0,0,0], 1))