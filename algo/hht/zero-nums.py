#coding: utf-8
import math


class Solution():
    def zeroNums(self, num):
        cnt = 0

        neg = False
        if num < 0:
            original = num = -num
            neg = True

        while num:
            num = num & (num - 1)
            cnt += 1

        if neg:
            prev = 32 - int(math.log(original, 2)) - 1
            cnt += prev

        return cnt


if __name__ == "__main__":
    print Solution().zeroNums(3)
    print Solution().zeroNums(8)
    print Solution().zeroNums(2)
    print Solution().zeroNums(-1)
    print Solution().zeroNums(-2)
