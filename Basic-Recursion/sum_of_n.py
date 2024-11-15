class Solution:
    def sumofSeries(self,n):
        if n==0:
            return 0
        return n+self.sumofSeries(n-1)
obj=Solution()
print(obj.sumofSeries(5))
print(obj.sumofSeries(10))
print(obj.sumofSeries(40))