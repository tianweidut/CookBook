
class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        if not matrix or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        r = []

        s = 0
        while 2 * s < m and 2 * s < n:
            end_m = m - s - 1
            end_n = n - s - 1
            # left -> right
            for i in range(s, end_n + 1):
                r.append(matrix[s][i])

            # up -> down
            if s < end_m:
                for i in range(s + 1, end_m + 1):
                    r.append(matrix[i][end_n])

            # right -> left
            if s < end_m and s < end_n:
                for i in range(end_n - 1, s - 1, -1):
                    r.append(matrix[end_m][i])

            # down -> up
            if s < end_m - 1 and s < end_n:
                for i in range(end_m - 1, s, -1):
                    r.append(matrix[i][s])

            s += 1

        return r

if __name__ == "__main__":
    s = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
         ]

    print Solution().spiralOrder(s)
    s = [[1,2,3]]
    print Solution().spiralOrder(s)

    s = [[1],[2],[3]]
    print Solution().spiralOrder(s)
