
class Solution:
    def maximum_subarray_with_sum_k(self,arr,k):
        max_len=0
        current_sum=0
        preffix={}
        n=len(arr)
        for i in range(n):
            current_sum+=arr[i]
            if current_sum==k:
                max_len=i+1
            if current_sum-k in preffix:
                max_len=max(max_len,i-preffix[current_sum-k])
            if current_sum not in preffix:
                preffix[current_sum]=i
        print(preffix)
        return max_len
obj=Solution()
resultant=obj.maximum_subarray_with_sum_k([1,-1,5,-2,3],3)
print("Length of the longest subarray of length k is: ",resultant)
