
class Solution:

    """
    @param A : An integer array
    @return : Two integer
    """

    def singleNumberIII(self, A):
        s = A[0]
        for a in A[1:]:
            s = s ^ a

        flag = 1
        while s & flag == 0:
            flag = flag << 1

        s1 = None
        s2 = None
        for a in A:
            if a & flag == 0:
                if s1 is None:
                    s1 = a
                else:
                    s1 = s1 ^ a
            else:
                if s2 is None:
                    s2 = a
                else:
                    s2 = s2 ^ a

        return s1, s2


if __name__ == "__main__":
    print Solution().singleNumberIII([-2147483648, 11, 10, 10, 11, 16, 0, 16, 32, 64, 64, 32])
