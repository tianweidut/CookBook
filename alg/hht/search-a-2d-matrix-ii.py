class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0

        i = 0
        j = len(matrix[0]) - 1

        cnt = 0
        while 0 <= i < len(matrix) and 0 <= j:
            if target == matrix[i][j]:
                cnt += 1
                i += 1
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1

        return cnt

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]]
    print Solution().searchMatrix(matrix, 3)
    print Solution().searchMatrix(matrix, 7)
