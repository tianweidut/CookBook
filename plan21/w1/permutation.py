#coding: utf-8

import copy

results = []

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        track = []
        self.do_permute(nums, track)
        return self.results
    
    def do_permute(self, nums, track):
        if len(track) == len(nums):
            import copy
            self.results.append(copy.copy(track))
            return
        
        for i in range(0, len(nums)):
            if nums[i] in track:
                continue
                
            track.append(nums[i])
            self.do_permute(nums, track)
            track.pop()

def permutation(nums):
	global results
	results = []

	ds = []
	do_permutation(nums, ds)
	return results


def do_permutation(nums, ds):
	if len(ds) == len(nums):
		results.append(copy.copy(ds))
		return

	for i in range(0, len(nums)):
		if nums[i] in ds:
			continue

		ds.append(nums[i])
		do_permutation(nums, ds)
		ds.pop()


if __name__ == "__main__":
	print(permutation([1,2,3]))
	print(permutation([1,2,3,4]))