class Solution:
    def findKRotation(self, arr):
        n=len(arr)
        low=0
        high=n-1
        index=-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if arr[low]<=arr[high]:
                if arr[low]<ans:
                    index=low
                    ans=arr[low]
                break
            if arr[low]<=arr[mid]:
                if arr[low]<ans:
                    index=low
                    ans=arr[low]
                low=mid+1
            if arr[mid]<=arr[high]:
                if arr[mid]<ans:
                    index=mid
                    ans=arr[mid]
                high=mid-1
        return index
obj=Solution()
result=obj.findKRotation([3,4,5,1,2])
print("Number of rotations in the sorted arrays is:",result)