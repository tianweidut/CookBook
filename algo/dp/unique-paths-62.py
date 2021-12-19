

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0] * n] * m

        for i in range(n):
            arr[m - 1][i] = 1

        for i in range(m):
            arr[i][n - 1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                arr[i][j] = arr[i + 1][j] + arr[i][j + 1]

        return arr[0][0]


if __name__ == "__main__":
    print Solution().uniquePaths(1, 2)
