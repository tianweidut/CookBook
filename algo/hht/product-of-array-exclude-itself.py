

class Solution:

    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, A):
        cnt = len(A)

        acc_f = acc_b = 1
        front = [1]
        back = [1]
        for i in range(cnt):
            acc_f *= A[i]
            acc_b *= A[cnt - i - 1]
            front.append(acc_f)
            back.append(acc_b)

        front.append(1)
        back.append(1)
        back = back[::-1]

        r = []
        for i in range(cnt):
            r.append(front[i] * back[i + 2])

        return r
