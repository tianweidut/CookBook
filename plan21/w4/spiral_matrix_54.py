class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        result = []
        while True:
            #1.left -> right
            for i in range(l, r+1):
                result.append(matrix[t][i])    
            t += 1
            if t > b: break
            #2.top -> bottom
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1
            if r < l: break
            #3.right -> left
            for i in range(r, l-1, -1):
                result.append(matrix[b][i])  
            b -= 1
            if b < t: break
            #4.bottom -> top
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l += 1
            if l > r: break
        
        return result