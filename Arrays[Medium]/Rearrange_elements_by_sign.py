class Solution:
    def rearrange_elements_by_size(self, nums):
        n = len(nums)
        ans = [0] * n
        posIndex = 0
        negIndex = 1

        for num in nums:
            if num < 0 and negIndex < n:
                ans[negIndex] = num
                negIndex += 2
            elif num >= 0 and posIndex < n:
                ans[posIndex] = num
                posIndex += 2

        # Append remaining numbers that couldn't be placed alternately
        remaining = [num for num in nums if num not in ans or ans.count(num) < nums.count(num)]
        for i in range(n):
            if ans[i] == 0 and remaining:
                ans[i] = remaining.pop(0)

        return ans


obj=Solution()
result=obj.rearrange_elements_by_size([3,1,-2,-5,2,4])
print("Rearranged the elements by sign ",result)