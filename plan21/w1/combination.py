#coding: utf-8

#输入1...n，k个为一组的所有组合

import copy

results = []

def combination(n, k):
	global results
	results = []
	ds = [] 
	do_combination(n, 1, k, ds)
	return results


def do_combination(n, start, k, ds):
	if len(ds) == k:
		results.append(copy.copy(ds))
		return

	for i in range(start, n +1):
		ds.append(i)
		do_combination(n, i+1, k, ds)
		ds.pop()

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.results = []
        
        track = []
        self.do_combine(n, k, 1, track)
        return self.results
    
    def do_combine(self, n, k, start, track):
        import copy

        if len(track) == k:
            self.results.append(copy.copy(track))
            return

        for i in range(start, n+1):
            track.append(i)
            self.do_combine(n, k, i+1, track)
            track.pop()

if __name__ == "__main__":
	print(combination(4,2))
	print(combination(4,1))
	print(combination(5,2))
	print(combination(5,3))
	print(combination(5,5))