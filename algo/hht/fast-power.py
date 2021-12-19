
class Solution:

    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        s = self.pow(a, n)
        return s % b

    def pow(self, a, n):
        if a <= 1:
            return a

        if n == 0:
            return 1
        elif n == 1:
            return a

        s = self.pow(a, n >> 1)
        s *= s
        if n & 1 == 1:
            s *= a

        return s

if __name__ == "__main__":
    #print Solution().fastPower(2, 10, 1)
    print Solution().fastPower(2, 2147483647, 2147483647)
