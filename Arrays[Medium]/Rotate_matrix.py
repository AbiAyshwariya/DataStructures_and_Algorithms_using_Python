class Solution:
    def rotate_matrix(self,matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix
obj=Solution()
result=obj.rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Rotated matrix is as follows: ",result)