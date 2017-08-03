
class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        row = 0

        r = [[0 for i in range(n)] for i in range(n)]
        cnt = 1

        while 2 * row < n:
            last_colum = n - row - 1
            last_row = n - row - 1

            for j in range(row, last_colum + 1):
                r[row][j] = cnt
                cnt += 1

            if row < last_row:
                for j in range(row + 1, last_row + 1):
                    r[j][last_colum] = cnt
                    cnt += 1

            if row < last_colum and row < last_row:
                for j in range(last_colum - 1, row - 1, -1):
                    r[last_row][j] = cnt
                    cnt += 1

            if row < last_row - 1 and row < last_colum:
                for j in range(last_row - 1, row, -1):
                    r[j][row] = cnt
                    cnt += 1

            row += 1

        return r
