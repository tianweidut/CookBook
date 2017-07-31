

class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.r = []
        candidates = sorted(candidates)
        self.dfs(candidates, 0, [], target)
        return self.r

    def dfs(self, candidates, pos, nums, target):
        import copy
        sum_nums = sum(nums)
        if sum_nums == target:
            self.r.append(copy.copy(nums))
            return
        elif sum_nums > target:
            return

        for i in range(pos, len(candidates)):
            self.dfs(candidates, i, nums + [candidates[i]], target)
