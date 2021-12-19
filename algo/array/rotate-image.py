

class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for layer in range(n / 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                top = matrix[first][i]
                offset = i - first

                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[first + offset][last]
                matrix[first + offset][last] = top


if __name__ == "__main__":
    print Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
