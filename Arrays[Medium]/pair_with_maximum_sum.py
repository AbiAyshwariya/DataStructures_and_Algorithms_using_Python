class Solution:
    def pairwitsum(self,arr):
        n=len(arr)
        if n<2:
            return None
        maxi=float('-inf')
        for i in range(n-1):
            pair_sum=arr[i]+arr[i+1]
            maxi=max(maxi,pair_sum)
        return maxi
obj=Solution()
result=obj.pairwitsum([4,5,7,8,3,-1])
print("Pair with Maximum sum is",result)