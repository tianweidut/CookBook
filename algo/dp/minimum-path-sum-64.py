
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        sz = [[0] * n for _ in range(m)]
        sz[m - 1][n - 1] = grid[m - 1][n - 1]

        asum = sz[m - 1][n - 1]
        for i in range(m - 2, -1, -1):
            asum += grid[i][n - 1]
            sz[i][n - 1] = asum

        asum = sz[m - 1][n - 1]
        for i in range(n - 2, -1, -1):
            asum += grid[m - 1][i]
            sz[m - 1][i] = asum

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                sz[i][j] = grid[i][j] + min(sz[i + 1][j], sz[i][j + 1])

        return sz[0][0]
