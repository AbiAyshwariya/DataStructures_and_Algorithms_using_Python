class Solution:
    def maximum_consecutive(self,arr):
        maxi=0
        cnt=0
        n=len(arr)
        for i in range(n):
            if arr[i]==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi
obj=Solution()
maximum=obj.maximum_consecutive([0,0,1,1,1,1,0,2,4,1,1,1])
print("Maximum length of consecutive ones are: ",maximum)