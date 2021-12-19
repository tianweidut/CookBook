#coding:utf-8


class Solution(object):
    def checkSubarraySumFor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cnt = len(nums)
        if cnt <= 1 or k <= 0:
            return False

        mem = [[None for i in range(0, cnt)] for j in range(cnt)]
        for i in range(cnt):
            mem[0][i] = nums[i]
            mem[i][0] = nums[i]
            mem[i][i] = nums[i]

        for i in range(0, cnt-1):
            for j in range(i+1, cnt):
                try:
                    mem[i][j] = mem[i][j-1] + nums[j]
                except:
                    print i, j
                    print nums[j]
                if mem[i][j] % k == 0:
                    return True

        return False

    def checkSubarraySum(self, nums, k):
        mem = {0: -1}
        rsum = 0

        for i, n in enumerate(nums):
            rsum += n
            
            if k != 0:
                rsum = rsum % k
            prev = mem.get(rsum)
            if prev is not None:
                if i - prev > 1:
                    return True
            else:
                mem[rsum] = i

        return False


if __name__ == "__main__":
    print Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
    print Solution().checkSubarraySum([23, 2, 6, 4, 7], 6)
    a = [422,224,184,178,189,290,196,236,281,464,351,193,49,76,0,298,193,176,158,514,312,143,475,322,206,67,524,424,76,99,473,256,364,292,141,186,190,69,433,205,93,72,476,393,512,468,160,201,226,394,47,140,389,51,142,135,349,244,16,356,440,188,16,133,58,394,7,517,56,480,400,146,169,439,102,374,370,242,4,264,120,218,196,173,215,411,501,321,319,147,369,458,319,174,379,46,129,353,330,101]
    print Solution().checkSubarraySum(a, 479)
