class Solution:
    def rotated_elements_by_k(self,arr,k):
        n=len(arr)
        k=k%n
        arr[:]=arr[-k:]+arr[:-k]
        return arr

obj=Solution()
rotated=obj.rotated_elements_by_k([1,2,3,4,5,6,7],3)
print("Array Rotated by K moves:",rotated)