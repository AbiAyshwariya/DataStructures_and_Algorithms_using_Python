
class Solution:
    def kadane_Algorithm(self,arr):
        current_sum=0
        maxi=arr[0]
        n=len(arr)
        for i in range(n):
            current_sum+=arr[i]
            maxi=max(maxi,current_sum)
            if current_sum<0:
                current_sum=0
        return maxi
obj=Solution()
result=obj.kadane_Algorithm([2,1,-3,4,-1,2,1,-5,4])
print("Sum of the Maximum Subarray is: ",result)
