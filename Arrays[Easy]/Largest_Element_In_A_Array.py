class Solution:
    def largest_element(self,arr):
        n = len(arr)
        max_index=0
        for i in range(1,n):
            max_index=i
        return arr[max_index]
obj=Solution()
largest=obj.largest_element([3,45,8,7,43,5,3,98])
print("Largest Element in the array is: ",largest)