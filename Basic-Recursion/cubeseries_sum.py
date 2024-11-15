class Solution:
    def sum_of_cube_series(self,n):
        if n==0:
            return 0
        return (n**3)+self.sum_of_cube_series(n-1)
obj=Solution()
print(obj.sum_of_cube_series(5))