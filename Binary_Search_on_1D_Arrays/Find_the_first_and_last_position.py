class Solution:
    def searchRange(self, nums, target) :
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_ans = findLeft(nums, target)
        right_ans = findRight(nums, target)
        if left_ans <= right_ans and left_ans <= len(nums) and nums[left_ans] == target:
            return [left_ans, right_ans]
        return [-1, -1]
obj=Solution()
result=obj.searchRange([5,7,8,8,10],8)
print("The First and Last Occurance of the element are:",result)