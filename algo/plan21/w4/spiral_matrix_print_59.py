class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0: return []
        
        matrix = [[0] * n for i in range(0, n)]
        l, r, t, b = 0, n-1, 0, n-1
        val = 1
        
        while True:
            #1.left ->right
            for i in range(l, r+1):
                matrix[t][i] = val
                val += 1
            t += 1
            if t > b: break
                
            #2. top -> bottom
            for i in range(t, b+1):
                matrix[i][r] = val
                val += 1
            r -= 1
            if l > r: break
                
            #3. right -> left
            for i in range(r, l-1, -1):
                matrix[b][i] = val
                val += 1
            b -= 1
            if t > b: break
            
            #4. bottom -> top
            for i in range(b, t-1, -1):
                matrix[i][l] = val
                val += 1
            l += 1
            if l > r: break
        
        return matrix