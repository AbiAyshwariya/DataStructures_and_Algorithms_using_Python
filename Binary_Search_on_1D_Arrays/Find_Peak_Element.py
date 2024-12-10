class Solution:
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-2]<nums[n-1]:
            return n-1
        left,right=1,n-2
        while left<=right:
            mid=(left+right)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return nums[mid]
            elif nums[mid]>nums[mid-1]:
                left=mid+1
            else:
                right=mid-1
        return -1
obj=Solution()
result=obj.findPeakElement([1,2,3,4,5,6,7,8,5,1])
print("Peak element which is greater than its neighbour in the array is: ",result)