class Solution:
    def hammingWeight_1(self, n: int) -> int:
        pos = 1
        res = 0
        for i in range (0, 32):
            if n & pos:
                res += 1
            pos = pos << 1
            
        return res
    
    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in range(0, 32) if n & 1 << i])