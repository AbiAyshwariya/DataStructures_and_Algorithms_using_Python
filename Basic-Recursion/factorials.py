class Solution:
    def factorials(self,n):
        if n==0:
            return 1
        return n*self.factorials(n-1)
obj=Solution()
print(obj.factorials(5))