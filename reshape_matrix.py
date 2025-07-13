# Given an m x n matrix mat, reshape it to r x c matrix. The reshaped matrix should be filled with all the elements of the original matrix 
# in the same row-traversing order as they were. If the reshape operation with given parameters is possible and legal, 
# output the new reshaped matrix; Otherwise, output the original matrix.
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m,n = len(mat),len(mat[0])
        if r*c!=m*n:
            return mat
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
        num = 0
        arr = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                arr[i][j] = tmp[num]
                num+=1
        return arr

def main():
    obj = Solution()
    print(obj.matrixReshape([[1,2],[3,4]],1,4))
    print(obj.matrixReshape([[1,2],[3,4]],2,4))
  
if __name__ == '__main__':
    main()
