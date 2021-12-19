class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k <= 0:
            return []
        
        self.k = k
        self.n = n
        self.r = []
        
        self.dfs(0, [])
        
        return self.r
        
    def dfs(self, index, array):
        a_cnt = len(array)
        if index > 9 or a_cnt > self.k:
            return
        
        if a_cnt == self.k:
            if sum(array) == self.n:
                self.r.append(array)
            return
        
        for i in range(index + 1, 10):
            if sum(array) + i > self.n:
                break
            
            self.dfs(i, array + [i])
            
