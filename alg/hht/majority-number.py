
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):

        val = None
        cnt = 0
        for n in nums:
            if val is None:
                val = n
                cnt += 1
            elif val == n:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    val = None

        return val

