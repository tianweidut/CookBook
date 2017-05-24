#coding: utf-8


class UnionFind(object):
    def __init__(self, n):
        self.nums = [i for i in range(n)]
        self.sz = [1] * n
        self.count = n

    def find(self, index):
        while index != self.nums[index]:
            self.nums[index] = self.nums[self.nums[index]]
            index = self.nums[index]
        return index

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)

        if ri == rj:
            return

        if self.sz[ri] < self.sz[rj]:
            self.sz[rj] += self.sz[ri]
            self.nums[ri] = rj
        else:
            self.sz[ri] += self.sz[rj]
            self.nums[rj] = ri

        self.count -= 1


class Solution(object):
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid_map = self.norm(grid)
        uf = UnionFind(len(grid_map))

        for i1, j1 in grid_map:
            for i2, j2 in grid_map:
                if i1 == i2 and j1 == j2:
                    continue

                if (abs(i1 - i2) == 1 and j1 == j2) or (abs(j1 - j2) == 1 and i1 == i2):
                    uf.union(grid_map[(i1, j1)], grid_map[(i2, j2)])

        return uf.count

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid_map = self.norm(grid)
        uf = UnionFind(len(grid_map))

        for i, j in grid_map:
            for n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if n in grid_map:
                    uf.union(grid_map[(i, j)], grid_map[n])

        return uf.count

    def norm(self, grid):
        grid_map = {}
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid_map[(i, j)] = cnt
                    cnt += 1

        return grid_map


def main():
    s = Solution()
    grid = ["11110","11010","11000","00000"]
    print s.numIslands(grid)

    s = Solution()
    grid = ["11000", "11000", "00100", "00011"]
    print s.numIslands(grid)


if __name__ == "__main__":
    main()
