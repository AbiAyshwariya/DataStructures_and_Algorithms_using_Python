class Solution:
    def search(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if the target is found
            if nums[mid] == target:
                return True

            # Handle duplicates by shrinking the search space
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Determine which part is sorted
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:  # Target in sorted left half
                    high = mid - 1
                else:  # Target in the right half
                    low = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:  # Target in sorted right half
                    low = mid + 1
                else:  # Target in the left half
                    high = mid - 1

        # Target is not found
        return False


# Example usage
obj = Solution()
result = obj.search([3, 2, 1, 3, 3, 3, 3], 1)
print("The target is present in the array:", result)
