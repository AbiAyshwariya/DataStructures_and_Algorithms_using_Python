class Solution:
    def findMin(self, nums):
        n=len(nums)
        low=0
        high=n-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans
obj=Solution()
result=obj.findMin([3,4,5,1,2])
print("The Minimum element in the sorted arrays is ",result)