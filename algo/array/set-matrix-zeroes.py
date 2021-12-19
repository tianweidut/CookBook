
class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l_rows = len(matrix)
        l_cols = len(matrix[0])

        rows = [False] * l_rows
        cols = [False] * l_cols

        for i in range(l_rows):
            for j in range(l_cols):
                k = matrix[i][j] == 0
                rows[i] |= k
                cols[j] |= k

        for i in range(l_rows):
            for j in range(l_cols):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
