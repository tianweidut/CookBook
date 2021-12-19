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
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_map = self.get_map(board)
        uf = UnionFind(len(board_map))

        for i, j in board_map:
            for n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if n in board_map:
                    uf.union(board_map[(i, j)]['index'], board_map[n]['index'])

        from collections import defaultdict
        uf_map = defaultdict(set)

        for i in board_map:
            root = uf.find(board_map[i]['index'])
            uf_map[root].add(i)

        for values in uf_map.values():
            has_bound = any([board_map[v]['is_bound'] for v in values])
            if has_bound:
                continue

            for i, j in values:
                board[i][j] = 'X'

    def get_map(self, board):
        board_map = {}
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    is_bound = i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1
                    board_map[(i, j)] = {'index': cnt, 'is_bound': is_bound}
                    cnt += 1

        return board_map


def main():
    s = Solution()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print board
    s = Solution()
    s.solve(board)
    print board

if __name__ == "__main__":
    main()
