class Solution:
    def factorials_less_than_n(self,n):
        factorials=[]
        fact=1
        i=1
        while fact<=n:
            factorials.append(fact)
            i+=1
            fact*=i
        return factorials
obj=Solution()
print(obj.factorials_less_than_n(5))
print(obj.factorials_less_than_n(15))