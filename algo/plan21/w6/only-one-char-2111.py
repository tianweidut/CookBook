class Solution:
    def firstUniqChar(self, s: str) -> str:
        from collections import defaultdict
        cmap = defaultdict(int)
        
        for c in s:
            cmap[c] += 1
            
        for c in s:
            if cmap[c] == 1:
                return c
            
        return ' '