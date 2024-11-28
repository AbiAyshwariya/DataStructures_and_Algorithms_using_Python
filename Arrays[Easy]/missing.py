class Solution:
    def missing(self,arr):
        n=len(arr)
        expected=n*(n+1)//2
        actual=sum(arr)
        return expected-actual

obj=Solution()
missing=obj.missing([0,1,3])
print("Missing element in the array is:",missing)