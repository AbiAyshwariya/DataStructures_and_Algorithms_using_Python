class Solution:
    def fibonacci(self,n):
        if n<=1:
            return n
        last=self.fibonacci(n-1)
        slast=self.fibonacci(n-2)
        return last+slast
obj=Solution()
print(obj.fibonacci(10))