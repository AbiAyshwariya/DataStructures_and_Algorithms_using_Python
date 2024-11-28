class Solution:
    def check_isSorted(self,arr):
        n=len(arr)
        sorted_nums=sorted(arr)
        for i in range(n):
            if arr[i:] + arr[:i]==sorted_nums:
                return True
        return False
obj=Solution()
result=obj.check_isSorted([4,5,1,2,3,4])
result1=obj.check_isSorted([4,5,2,1,2,3,0,4])
print("Array is sorted:",result)
print("Array is sorted:",result1)
