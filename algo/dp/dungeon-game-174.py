

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        import sys
        m = len(dungeon)
        n = len(dungeon[0])
        sz = [[sys.maxint] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down = sys.maxint if i == m - 1 else sz[i + 1][j]
                right = sys.maxint if j == n - 1 else sz[i][j + 1]

                min_health = 1 if i == m - 1 and j == n - 1 else min(down, right)
                if dungeon[i][j] >= min_health:
                    sz[i][j] = 1
                else:
                    sz[i][j] = min_health - dungeon[i][j]

        return sz[0][0]

if __name__ == "__main__":
    s = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]
    print Solution().calculateMinimumHP(s)
