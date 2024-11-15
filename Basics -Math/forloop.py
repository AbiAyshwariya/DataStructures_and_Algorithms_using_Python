class Solution:
    def forloop(self,n)->int:
        f1,f2=1,1
        for i in range(3,n+1):
            f1,f2=f2,f1+f2
        return f2

n=int(input())
obj=Solution()
print(obj.forloop(n))

