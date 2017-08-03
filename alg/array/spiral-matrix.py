
class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        row = 0
        cnt_rows = len(matrix)
        cnt_colums = len(matrix[0])
        r = []

        while 2 * row < cnt_rows and 2 * row < cnt_colums:
            last_colum = cnt_colums - row - 1
            last_row = cnt_rows - row - 1

            for j in range(row, last_colum + 1):
                r.append(matrix[row][j])

            if row < last_row:
                for j in range(row + 1, last_row + 1):
                    r.append(matrix[j][last_colum])

            if row < last_row and row < last_colum:
                for j in range(last_colum - 1, row - 1, -1):
                    r.append(matrix[last_row][j])

            if row < last_row - 1 and row < last_colum:
                for j in range(last_row - 1, row, -1):
                    r.append(matrix[j][row])

            row += 1
        return r
