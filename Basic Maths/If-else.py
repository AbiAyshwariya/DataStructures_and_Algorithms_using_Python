class Solution:
    def compareNM(self,n:int,m:int)->str:
        if(n>m):
            return "greater"
        elif(n==m):
            return "equal"
        elif(n<m):
            return "lesser"
        else:
            return -1
        
obj=Solution()
print(obj.compareNM(4,5))
print(obj.compareNM(7,6))
print(obj.compareNM(4,4))
