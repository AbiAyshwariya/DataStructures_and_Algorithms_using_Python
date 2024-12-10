class Solution:
    def merge_overlapping(self,nums):
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            if not ans or nums[i][0]>ans[-1][1]:
                ans.append(nums[i])
            else:
                ans[-1][1]=max(ans[-1][1],nums[i][-1])
        return ans
obj=Solution()
result=obj.merge_overlapping([[1,3],[2,6],[8,9],[2,4],[15,18],[16,17]])
print("Merged Overlapping Subarrays are as follows: ",result)