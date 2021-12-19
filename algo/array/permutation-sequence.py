
class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not k:
            return ""

        nums = [i for i in range(1, n + 1)]

        fb = [1] * (n + 2)
        for i in range(1, n + 1):
            fb[i] = fb[i - 1] * i

        import math
        x = n
        r = ""
        for i in range(0, n):
            pos = int(math.ceil(float(k) / fb[x - 1]))
            number = nums[pos - 1]
            nums.remove(number)
            r += str(number)

            k = k % fb[x - 1]
            x = x - 1

        return r
