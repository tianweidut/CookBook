class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col-1
        
        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
                
        return False