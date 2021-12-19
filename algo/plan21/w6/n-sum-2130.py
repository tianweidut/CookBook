class Solution:
    def sumNums(self, n: int) -> int:
        self.res = 0
        def _s(n):
            n > 1 and _s(n-1)
            self.res += n
        
        _s(n)
        return self.res