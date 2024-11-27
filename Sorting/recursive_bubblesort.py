class Solution:
    def bubble_sort(self,arr,n):
        if n<=1:
            return n
        did_swap=False
        for j in range(n-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                did_swap=True
        if not did_swap:
            return
        self.bubble_sort(arr,n-1)

if __name__  == "__main__":
    arr=[5,7,6,4,3,66,77,34,21]
    n=len(arr)-1
    obj=Solution()
    obj.bubble_sort(arr,n)
    print("Sorted Array: ",arr)
