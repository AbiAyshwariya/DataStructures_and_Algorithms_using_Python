class Solution:
    def bubble_sort(self,arr):
        n=len(arr)
        for i in range(n-1,0,-1):
            swapped=False
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if not swapped:
                break
        return arr

obj=Solution()
print(obj.bubble_sort([5,6,3,2,6,7,9,3,6]))
