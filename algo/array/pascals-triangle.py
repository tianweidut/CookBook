
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        r = []
        for row in range(0, numRows):
            sr = []
            row_cnt = row + 1
            for colum in range(0, row_cnt):
                if colum == 0 or colum == row or row == 0:
                    sr.append(1)
                else:
                    sr.append(r[row - 1][colum - 1] + r[row - 1][colum])
            r.append(sr)

        return r
