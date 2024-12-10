class Solution:
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
obj=Solution()
result=obj.search([7,8,9,1,2,3,4,5,6],1)
print("The element target is found at the index:",result)