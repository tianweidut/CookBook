
class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code

    def grayCode(self, n):
        import math

        if n <= 0:
            return [0]
        elif n == 1:
            return [0, 1]

        target = int(math.pow(2, n))

        prev = 0
        seq = [0]

        self.seq = []
        self.flag = False
        self.do_gray(prev, n, seq, target)
        return self.seq

    def do_gray(self, prev, n, seq, target):
        if self.flag:
            return

        if len(seq) == target:
            self.seq = seq
            self.flag = True
            return

        m = 1
        for i in range(n):
            if prev & m == 0:
                next = prev | m
            else:
                next = prev & ~m

            if next not in seq and next <= target:
                self.do_gray(next, n, seq + [next], target)

            m = m << 1


if __name__ == "__main__":
    print Solution().grayCode(5)
