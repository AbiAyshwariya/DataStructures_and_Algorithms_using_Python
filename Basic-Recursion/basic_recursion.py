
class Solution:
    i=1
    def printNos(self,n,i=1):
        if i>n:
            return
        print(i,end=" ")
        self.printNos(n,i+1)

obj=Solution()
obj.printNos(10)
