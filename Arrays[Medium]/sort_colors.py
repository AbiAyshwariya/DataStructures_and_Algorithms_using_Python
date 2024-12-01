from django.db.models.expressions import result
from numpy.ma.core import array


class Solution:
    def sort_colors(self,arr):
        n=len(arr)
        low,mid=0,0
        high=n-1
        while mid<=high:
            if arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid]
                mid+=1
                low+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1
        return arr

obj=Solution()
result=obj.sort_colors([0,0,0,0,1,0,2,2,0,1,0,1,2,2,2,1,1,1,0])
print("Sorted Array with grouped elements of 0's 1's and 2's:",result)