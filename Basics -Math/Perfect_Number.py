class Solution:
    def perfect_number(self,n):
        original=n
        sum_1=1
        if(n==0):
            return 1
        for i in range(2,int(n*0.5)+1):
            if(n%i==0):
                sum_1+=i
        return original==sum_1
obj=Solution()
print(obj.perfect_number(6))
