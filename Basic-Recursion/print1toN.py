class Solution:
    def printnum(self,n,i=0)->int:
        if i>n:
            return 0
        print(i)
        self.printnum(n,i+1)
obj=Solution()
obj.printnum(10)


