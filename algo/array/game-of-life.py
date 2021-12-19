
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        nb = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for row in range(len(board)):
            for colum in range(len(board[0])):
                lives = sum([self.get_lives(board, row + x, colum + y) for x, y in nb])
                
                if lives == 3 or (lives == 2 and board[row][colum] == 1):
                    board[row][colum] |= 2
                    
        for row in range(len(board)):
            for colum in range(len(board[0])):
                board[row][colum] = board[row][colum] >> 1
                    
    def get_lives(self, board, row, colum):
        if row < 0 or colum < 0 or row >= len(board) or colum >= len(board[0]):
            return 0
        return board[row][colum] & 1
