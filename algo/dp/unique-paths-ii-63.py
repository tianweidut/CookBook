

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        sz = [[0] * n for i in range(m)]

        has_obstacle = False
        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][n - 1] == 1 or has_obstacle:
                has_obstacle = True
                sz[i][n - 1] = 0
            else:
                sz[i][n - 1] = 1

        has_obstacle = False
        for i in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][i] == 1 or has_obstacle:
                has_obstacle = True
                sz[m - 1][i] = 0
            else:
                sz[m - 1][i] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    sz[i][j] = sz[i + 1][j] + sz[i][j + 1]

        return sz[0][0]


if __name__ == "__main__":
    print Solution().uniquePathsWithObstacles([[0,1],[0,0]])
