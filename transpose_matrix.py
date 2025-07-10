# Given a 2D integer array matrix (not necessarily square matrix), return the transpose of matrix
class Solution(object):
    def transpose2DMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(matrix),len(matrix[0])
        matrix_2 = [[0]*m for _ in range(n)] 
        for i in range(m):
            for j in range(n):
                matrix_2[j][i] = matrix[i][j]
        return matrix_2
    def transposeSquareMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix
  
