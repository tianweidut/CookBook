

class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        if n <= 0:
            return []

        self.r = []
        for i in range(0, 10):
            self.num_print(str(i), 0, n)

        return self.r[1:]

    def num_print(self, num, index, n):
        if index == n - 1:
            self.r.append(int(num))
            return

        for i in range(0, 10):
            self.num_print(num + str(i), index + 1, n)


if __name__ == "__main__":
    s = Solution().numbersByRecursion(6)
