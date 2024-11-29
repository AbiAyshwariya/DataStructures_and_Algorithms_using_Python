class Solution:
    def longest_subarray(self,arr,k):
        max_len=0
        sum=arr[0]
        left,right=0,0
        n=len(arr)
        while right < n:
            while sum>k and left<=right:
                sum-=arr[left]
                left+=1
            if sum==k:
                max_len=max(max_len,right-left+1)
            right+=1
            if right<n:
                sum+=arr[right]
        return max_len
obj=Solution()
result=obj.longest_subarray([4,1,1,2,1,1],10)
print("Length of the longest subarray with sum k is:",result)