
class Solution(object):

    def maxRotateFunction_all(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import sys
        if not A:
            return 0

        max_sum = -sys.maxsize - 1
        len_a = len(A)

        for i in range(len_a):
            r = 0
            cnt = 0
            for j in range(len_a):
                k = (i + j) % len_a
                r += cnt * A[k]
                cnt += 1
            max_sum = max(r, max_sum)

        return max_sum

    def maxRotateFunction(self, A):
        a_all = sum(A)
        len_a = len(A)
        f = sum([i * j for i, j in zip(A, range(len_a))])
        max_sum = f

        for i in range(0, len_a - 1):
            f = f - a_all + len_a * A[i]
            max_sum = max(f, max_sum)

        return max_sum

if __name__ == "__main__":
    print Solution().maxRotateFunction([4, 3, 2, 6])
