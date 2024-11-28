class Solution:
    def second_largest(self,arr):
        n=len(arr)
        if n<=2:
            return None
        first=second=float('-inf')
        for num in arr:
            if num>first :
                second=first
                first=num
            elif num>second and num!=first:
                second=num
        if second == float('-inf'):
            return -1
        return second

obj=Solution()
second_large=obj.second_largest([3,6,5,4,6,7,8,8])
print("Second Largest element in the array: ",second_large)