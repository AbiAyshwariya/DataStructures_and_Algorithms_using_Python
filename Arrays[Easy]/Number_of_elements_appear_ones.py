class Solution:
    def number_of_ones_count(self,arr):
        n=len(arr)
        xor=0
        for i in range(n):
            xor=xor^arr[i]
        return xor
obj=Solution()
result=obj.number_of_ones_count([1,1,2,3,3,4,4])
print("Number that appears only ones in the array is: ",result)