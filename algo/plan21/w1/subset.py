#coding: utf-8
import copy

results = []

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        track = []
        self.do_subsets(nums, 0, track)
        return self.results
    
    def do_subsets(self, nums, start, track):
        import copy
        self.results.append(copy.copy(track))
        
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.do_subsets(nums, i+1, track)
            track.pop()

def subset(ds):
	rs = []
	do_subset(ds, 0, rs)
	return results


def do_subset(ds, start, rs):
	results.append(copy.copy(rs))

	for i in range(start, len(ds)):
		rs.append(ds[i])
		do_subset(ds, i + 1, rs)
		rs.pop()

if __name__ == "__main__":
	print(subset([1,2,3]))
	print(subset([1,2,3,]))