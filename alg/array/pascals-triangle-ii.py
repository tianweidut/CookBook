
class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [0] * (rowIndex + 1)
        r[0] = 1

        for row in range(1, rowIndex + 1):
            for colum in range(row, 0, -1):
                r[colum] += r[colum - 1]

        return r
