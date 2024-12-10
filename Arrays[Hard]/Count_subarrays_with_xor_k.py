class Solution:
    def count_subbarry_with_xor_k(self,arr,k):
        n=len(arr)
        xr=0
        mpp={}
        mpp={0:1}
        cnt=0
        for i in range(n):
            xr=xr^arr[i]
            if xr^k in mpp:
                cnt+=mpp[xr^k]
            mpp[xr]=mpp.get(xr,0)+1
        return cnt
obj=Solution()
result=obj.count_subbarry_with_xor_k([4,2,2,6,4],6)
print("Longest Subarray with xor as k :",result)

