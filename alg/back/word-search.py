
class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False

        self.word = word
        self.board = board
        self.rows = len(board)
        self.colums = len(board[0])
        self.r = False

        for i in range(0, self.rows):
            for j in range(0, self.colums):
                self.dfs(0, [], (i, j))

        return self.r

    def dfs(self, w_pos, path, pos):
        if self.r:
            return

        if self.board[pos[0]][pos[1]] != self.word[w_pos]:
            return
        w_pos += 1

        if w_pos == len(self.word):
            self.r = True
            return

        neighbor_pos = []
        for i in (-1, 1):
            if 0 <= pos[1] + i < self.colums:
                neighbor_pos.append((pos[0], pos[1] + i))
            if 0 <= pos[0] + i < self.rows:
                neighbor_pos.append((pos[0] + i, pos[1]))

        for p in neighbor_pos:
            i, j = p
            if p not in path:
                self.dfs(w_pos, path + [pos], p)
