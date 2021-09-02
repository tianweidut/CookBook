class Solution:
    def subarraySum_slow(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
            
        ans = 0
        for j in range(1, len(nums) + 1):
            for i in range(0, j):
                if prefix_sum[j] - prefix_sum[i] == k:
                    ans += 1
        return ans
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        nmap = defaultdict(int)
        nmap[0] = 1
        
        prefix = 0
        ans = 0
        
        for n in nums:
            prefix += n
            ans += nmap.get(prefix - k, 0)
            nmap[prefix] += 1
            
        return ans
