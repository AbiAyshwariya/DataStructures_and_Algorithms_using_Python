import math
class Solution:
    def check_prime(self,n):
        count=0
        for i in range(1,n*n+1):
            if n%i==0:
                count=count+1
        if(count>1):
            return True
        else:
            return False

obj=Solution()
print(obj.check_prime(7))
