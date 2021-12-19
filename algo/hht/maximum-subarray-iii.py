
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        len_nums = len(nums)
        if len_nums < k:
            return 0
            
        import sys
        min_v = - sys.maxint - 1
        
        local_m = [[0 for i in range(k + 1)] for j in range(len_nums + 1)]
        global_m = [[0 for i in range(k + 1)] for j in range(len_nums + 1)]
        
        for j in range(1, k + 1):
            local_m[j-1][j] = min_v
            for i in range(j, len_nums + 1):
                local_m[i][j] = max(global_m[i-1][j-1], local_m[i-1][j]) + nums[i - 1]
                
                if i == j:
                    global_m[i][j] = local_m[i][j] 
                else:
                    global_m[i][j] = max(global_m[i-1][j], local_m[i][j])
                
        return global_m[len_nums][k]

#https://zhengyang2015.gitbooks.io/lintcode/maximum_subarray_iii_43.html
