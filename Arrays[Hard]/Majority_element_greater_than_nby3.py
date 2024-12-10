class Solution:
    def majorityElement(self, nums):
        cnt1 = 0
        cnt2 = 0
        ele1, ele2 = float('-inf'), float('-inf')
        n = len(nums)
        for i in range(n):
            if cnt1 == 0 and nums[i] != ele2:
                cnt1 += 1
                ele1 = nums[i]
            elif cnt2 == 0 and nums[i] != ele1:
                cnt2 += 1
                ele2 = nums[i]
            elif ele1 == nums[i]:
                cnt1 += 1
            elif ele2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt3, cnt4 = 0, 0
        for i in range(n):
            if nums[i] == ele1:
                cnt3 += 1
            if nums[i] == ele2:
                cnt4 += 1
        ls = []
        if cnt3 > n // 3:
            ls.append(ele1)
        if cnt4 > n // 3:
            ls.append(ele2)
        return ls

obj=Solution()
result=obj.majorityElement([1,1,1,3,3,2,2,2])
print("Element that occurs more than n//3 times are:",result)

