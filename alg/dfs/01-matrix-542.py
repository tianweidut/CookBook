

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix

        xcnt = len(matrix)
        ycnt = len(matrix[0])

        for i in range(xcnt):
            for j in range(ycnt):
                if matrix[i][j] == 0:
                    continue
                marked = [[0] * ycnt] * xcnt
                matrix[i][j] = self.find_distance(matrix, i, j, marked)

        return matrix

    def find_distance(self, matrix, i, j, marked):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 1000000

        if marked[i][j]:
            return matrix[i][j]

        if matrix[i][j] == 0:
            return 0
        else:
            marked[i][j] = 1
            return min(self.find_distance(matrix, i - 1, j, marked),
                       self.find_distance(matrix, i + 1, j, marked),
                       self.find_distance(matrix, i, j - 1, marked),
                       self.find_distance(matrix, i, j + 1, marked)) + matrix[i][j]


if __name__ == "__main__":
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]]

    print Solution().updateMatrix(matrix)

    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]

    print Solution().updateMatrix(matrix)
