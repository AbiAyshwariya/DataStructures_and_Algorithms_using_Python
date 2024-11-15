class Solution:
    def counter(self,n):
        count=0
        original=n
        while n>0:
            rem=n%10
            if rem!=0 and original%10==0:
                count=count+1
            n=n//10
        return count

obj=Solution()
print(obj.counter(12))
print(obj.counter(50))
