class Solution:
    def printnumbers(self,n)->int:
        if n<0:
            return 0
        print(n)
        self.printnumbers(n-1)

obj=Solution()
obj.printnumbers(10)
