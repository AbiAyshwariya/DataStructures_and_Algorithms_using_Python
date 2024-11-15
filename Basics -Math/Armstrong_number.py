class Solution:
    def armstrong(self,n):
        count=0
        sum_1=0
        original=n
        while(n>0):
            rem=n%10
            count=count+1
            n=n//10
        n=original
        while n>0:
            rem=n%10
            sum_1+=rem**count
            n=n//10
        return sum_1==original
obj=Solution()
print(obj.armstrong(153))

