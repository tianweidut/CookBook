
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        r = []
        factor = 1

        for d in digits[::-1]:
            num = (d + factor) % 10
            factor = (d + factor) / 10
            r.append(num)

        if factor:
            r.append(factor)

        return r[::-1]
