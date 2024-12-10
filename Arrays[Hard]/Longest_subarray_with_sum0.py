class Solution:
    def longest_subarray(self,arr):
        sum=0
        maxi=0
        mpp={}
        n=len(arr)
        for i in range(n):
            sum+=arr[i]
            if sum==0:
                maxi=i+1
            else:
                if sum in mpp:
                    maxi=max(maxi,i-mpp[sum])
                else:
                    mpp[sum]=i
        return maxi
obj=Solution()
result=obj.longest_subarray([15,-2,2,-8,1,7,10,23])
print("Longest Subarray with sum as 0:",result)