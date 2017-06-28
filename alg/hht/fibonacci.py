
class Solution:
    # @param n: an integer
    # @return an integer f(n)

    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0

        if n == 2:
            return 1

        # return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        a, b = 0, 1

        for i in range(3, n + 1):
            t = b
            b = a + b
            a = t

        return b
