class Solution:
    def binary_search(self,nums,low,high,target):
        if low>high:
            return -1
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.binary_search(nums,low,mid-1,high,target)
        return self.binary_search(nums,mid+1,high,target)
    def search(self,nums,target):
        return self.binary_search(nums,0,len(nums)-1,target)
obj=Solution()
nums=[1,2,3,4,5,6]
result=obj.search([1,2,3,4,5,6],3)
print("Element is found at the index: ",result)
