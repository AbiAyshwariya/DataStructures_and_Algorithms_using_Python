class Solution:
    def upper_bound(self,arr,k):
        n=len(arr)
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
obj=Solution()
result=obj.upper_bound([2,4,6,7],6)
print("Upper Bound of the arrays is:",result)