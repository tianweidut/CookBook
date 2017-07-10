# coding: utf-8


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 0 or 1 < n < 4:
            return []
        elif n == 1:
            return [['Q']]

        self.r = []

        row = 0
        p = [None] * n
        self.dfs(row, n, p)

        str_r = []
        for rr in self.r:
            m = [['.' for i in range(n)] for j in range(n)]
            for i, j in enumerate(rr):
                m[i][j] = 'Q'
            str_r.append(["".join(mm) for mm in m])

        return str_r

    def dfs(self, row, n, p):
        import copy
        p = copy.copy(p)
        if row == n:
            self.r.append(p)
            return

        for col in range(n):
            if not self.chk(row, col, p):
                continue

            p[row] = col
            self.dfs(row + 1, n, p)

    def chk(self, row, col, p):
        for i in range(0, row):
            if abs(row - i) == abs(col - p[i]) or col == p[i]:
                return False

        return True
