class Solution:
    def count_digits(self,x)->int:
        count=0
        while(x>0):
            rem=x%10
            count=count+1
            x=x//10
        return count
obj=Solution()
print(obj.count_digits(7889))
print(obj.count_digits(987678))


