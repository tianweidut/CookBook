
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import sys
        from Queue import Queue
        if not matrix:
            return matrix

        xcnt, ycnt = len(matrix), len(matrix[0])
        q = Queue()

        for i in range(xcnt):
            for j in range(ycnt):
                if matrix[i][j] == 0:
                    q.put((i, j))
                else:
                    matrix[i][j] = sys.maxint

        while not q.empty():
            curx, cury = q.get()

            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nebx, neby = curx + x, cury + y

                if nebx < 0 or neby < 0 or nebx >= xcnt or neby >= ycnt:
                    continue

                if matrix[nebx][neby] > matrix[curx][cury] + 1:
                    matrix[nebx][neby] = matrix[curx][cury] + 1
                    q.put((nebx, neby))

        return matrix


if __name__ == "__main__":
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]]

    print Solution().updateMatrix(matrix)

    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]

    print Solution().updateMatrix(matrix)
