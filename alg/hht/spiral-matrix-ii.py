
class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        if n < 0:
            return []

        matrix = [[0] * n for i in range(n)]
        
        print matrix
        val = 1
        s = 0
        while 2 * s < n:
            end_x = n - s - 1
            end_y = n - s - 1
            for i in range(s, end_y + 1):
                matrix[s][i] = val
                val += 1

            if s < end_y:
                for i in range(s + 1, end_x + 1):
                    matrix[i][end_y] = val
                    val += 1

            if s < end_x and s < end_y:
                for i in range(end_y - 1, s - 1, -1):
                    matrix[end_x][i] = val
                    val += 1

            if s < end_x - 1 and s < end_y:
                for i in range(end_x - 1, s, -1):
                    matrix[i][s] = val
                    val += 1
            s += 1
        return matrix


if __name__ == "__main__":
    print Solution().generateMatrix(3)
