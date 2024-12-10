class Solution:
    def maximum_product(self,nums):
        n=len(nums)
        pref,suff=1,1
        ans=float('-inf')
        for i in range(n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[n-i-1]
            ans=max(ans,max(pref,suff))
        return ans
obj=Solution()
result=obj.maximum_product([2,3,-2,4])
print("Maximum Product Subarray is :",result)