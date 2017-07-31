
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        self.r = []

        candidates = sorted(candidates)
        self.n = len(candidates)

        self.dfs(candidates, 0, [], target)

        return self.r

    def dfs(self, candidates, pos, nums, target):
        sum_nums = sum(nums)
        import copy
        if sum_nums == target:
            self.r.append(copy.copy(nums))
            return

        if pos == self.n or sum_nums > target:
            return

        for i in range(pos, self.n):
            if i > pos and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, i + 1, nums + [candidates[i]], target)
