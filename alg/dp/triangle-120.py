

class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle[-1])

        sz = []
        for i in range(1, n + 1):
            sz.append([0] * i)

        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                if i == n - 1:
                    sz[i][j] = triangle[i][j]
                else:
                    sz[i][j] = triangle[i][j] + min(sz[i + 1][j], sz[i + 1][j + 1])

        return sz[0][0]


if __name__ == "__main__":
    s = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print Solution().minimumTotal(s)
