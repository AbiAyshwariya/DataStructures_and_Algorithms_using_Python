class Solution:
    def whileloop(self, n:int):
        multiplier=10
        while(multiplier>0):
            print(n*multiplier,end=" ")
            multiplier=multiplier-1
obj=Solution()
obj.whileloop(5)