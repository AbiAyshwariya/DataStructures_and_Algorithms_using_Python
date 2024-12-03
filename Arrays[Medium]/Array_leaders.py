class Solution:
    def array_leaders(self,arr):
        n=len(arr)
        maxi=arr[-1]
        leaders=[]
        leaders.append(maxi)
        for i in range(n-2,-1,-1):
            if arr[i]>maxi:
                leaders.append(arr[i])
                maxi=arr[i]
        return leaders[::-1]
obj=Solution()
result=obj.array_leaders([16,17,4,3,5,2])
print("Array Leaders which has no greater elements on its right are:",result)