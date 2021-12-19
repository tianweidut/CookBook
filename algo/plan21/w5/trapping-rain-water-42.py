class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        lmax = [height[0]]
        rmax = [height[-1]]
        
        for i in range(1, len(height)):
            lmax.append(max(height[i], lmax[i-1]))
            
        for i in range(1, len(height)):
            rmax.append(max(height[len(height) - 1 - i], rmax[i-1]))
        rmax = rmax[::-1]
            
        ans = 0
        for i in range(1, len(height)-1):
            ans += min(lmax[i], rmax[i]) - height[i]
            
        return ans