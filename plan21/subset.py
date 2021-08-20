#coding: utf-8
import copy

results = []

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