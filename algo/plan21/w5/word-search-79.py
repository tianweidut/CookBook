class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or board[0] is None: return False
        
        row, col = len(board), len(board[0])
        visited = {}
        
        def dfs(wi, bi, bj):
            if wi == len(word): return True
            
            if (bi < 0 or bi >= row or
                bj < 0 or bj >= col or
                visited.get((bi, bj)) or
                board[bi][bj] != word[wi]):
                return False
            
            visited[(bi, bj)] = True
            r = dfs(wi+1, bi+1, bj) or dfs(wi+1, bi-1, bj) or dfs(wi+1, bi, bj+1) or dfs(wi+1, bi, bj-1)
            visited[(bi, bj)] = False
            return r
        
        for i in range(0, row):
            for j in range(0, col):
                r = dfs(0, i, j)
                if r:
                    return True
                
        return False