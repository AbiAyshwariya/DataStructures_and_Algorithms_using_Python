class Solution:
    def som_of_divisors(self,n):
        divisors_sum=[0]*(n+1)
        for i in range(1,n+1):
            for j in range(i,n+1,i):
                divisors_sum[j]+=i
        return sum(divisors_sum)

obj=Solution()
print(obj.som_of_divisors(4))