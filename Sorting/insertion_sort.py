class Solution:
    def insertion_sort(self,arr):
        n=len(arr)
        for i in range(n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j=j-1
        return arr
obj=Solution()
print(obj.insertion_sort([7,5,3,5,7,8,1,2]))