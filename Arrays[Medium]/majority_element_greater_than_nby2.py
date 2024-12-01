class Solution:
    def greater_element(self,arr):
        cnt=0
        n=len(arr)
        for i in range(n):
            if cnt==0:
                cnt=1
                ele=arr[i]
            elif arr[i]==ele:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(n):
            if arr[i]==ele:
                cnt1+=1
        if cnt1>n//2:
            return ele
        return []
obj=Solution()
result=obj.greater_element([2,2,2,6,2,7,2,1,2])
print("Element that appears more than n//2 times is :",result)