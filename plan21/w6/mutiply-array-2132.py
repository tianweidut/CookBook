class Solution:
    def constructArr2(self, a: List[int]) -> List[int]:
        if a is None or len(a) == 0:
            return []
        
        n = len(a)
        matrix = [[1] * (n+2) for i in range(0, n+2)]
        for i in range(1, n+1):
            for j in range(i, n+1):
                matrix[i][j] = a[i-1] if i == j else matrix[i][j-1] * a[j-1]
        
        res = [0] * n
        for i in range(1, n+1):
            res[i-1] = matrix[1][i-1] * matrix[i+1][n]
        
        return res
    
    def constructArr(self, a):
        if a is None or len(a) == 0:
            return []
        
        n = len(a)
        left = [1] * (n+2)
        for i in range(1, n+1):
            left[i] = left[i-1] * a[i-1]
            
        right = [1] * (n+2)
        for i in range(1, n+1):
            right[i] = right[i-1] * a[n-i]
            
        res = [0] * n
        for i in range(0, n):
            res[i] = left[i] * right[n-1-i]
            
        return res