class Solution:
    def lower_bound(self,arr,k):
        n=len(arr)
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
obj=Solution()
result=obj.lower_bound([3,5,8,15,19],8)
print("Lower bound of the given target : ",result)
