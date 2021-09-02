
class Solution:
    def twoSum(self, nums, target):
		nums.sort() 

		start = 0
		end = len(nums) -1 
		while start < end:
			if target == nums[start] + nums[end]:
				return [start, end]
			elif target > nums[start] + nums[end]:
				start += 1
			else:
				end -= 1

		return []