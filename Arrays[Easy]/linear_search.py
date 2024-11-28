class Solution:
    def linear_search(self,arr,k):
        n=len(arr)
        for i in range(n):
            if arr[i]==k:
                return i
        return -1
obj=Solution()
found=obj.linear_search([1,2,4,5,6,7,8],7)
print("Element is found at index:",found)
