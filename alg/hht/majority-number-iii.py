class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        from collections import defaultdict
        
        n_hash = defaultdict(int)
        main_cnt = len(nums) / float(k) 
        
        for n in nums:
            n_hash[n] += 1
            if n_hash[n] > main_cnt:
                return n
