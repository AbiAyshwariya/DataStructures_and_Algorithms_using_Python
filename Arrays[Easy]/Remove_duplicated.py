from jedi.settings import dynamic_params
from pygments.util import duplicates_removed


class Solution:
    def remove_duplicated(self,arr):
        n=len(arr)
        i=0
        for j in range(1,n):
            if arr[j]!=arr[i]:
                arr[i+1]=arr[j]
                i+=1
        return i+1

obj=Solution()
duplicates_removed=[]
duplicates_removed=obj.remove_duplicated([1,1,2,3,4,4,5,5,5])
print("Number of unique elements in the Array:",duplicates_removed)