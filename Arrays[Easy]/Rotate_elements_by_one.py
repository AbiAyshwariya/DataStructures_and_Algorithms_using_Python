class Solution:
    def Rotate_elements_by_one(self,arr):
        n=len(arr)
        if n<=1:
            return -1
        temp=arr[n-1]
        for i in range(n-1,-1,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        return arr

obj=Solution()
rotated=obj.Rotate_elements_by_one([1,2,3,4,5,6])
print("Left Rotated Element by one:",rotated)