# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        last = n

        while start <= end:
            mid = (end - start) / 2 + start
            if isBadVersion(mid):
                last = mid
                end = mid - 1
            else:
                start = mid + 1

        return last
