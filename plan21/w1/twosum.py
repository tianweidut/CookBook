#coding: utf-8

# 1. 排序后start/end指针
# 2. 两次遍历，通过map-index记录

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        nmap = defaultdict(list)
        
        for i, v in enumerate(nums):
            nmap[v].append(i)
            
        for i, v in enumerate(nums):
            for j in nmap.get(target - v, []):
                if j == i: continue
                
                return [i, j]
        return []

def two_sum(target, nums):
	nmap = defaultdict(list)

	for i in range(0, len(nums)):
		nmap[nums[i]].append(i)

	for i in range(0, len(nums)):
		find = target - nums[i]
		if find not in nmap:
			continue
		
		for j in nmap.get(target-nums[i], []):
			if j == i:
				continue

			return [i, j]

	return []


if __name__ == "__main__":
	print(two_sum(6, [3,1,3,6]))