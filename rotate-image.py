class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # inverse rows
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n-col-1] = matrix[row][n-col-1], matrix[row][col]
