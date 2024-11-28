class Solution:
    def moves_zeros_to_end(self,arr):
        n=len(arr)
        j=0
        for i in range(j+1,n):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr

obj=Solution()
rotated=obj.moves_zeros_to_end([0,0,1,2,3,0,4,0,7,7,0])
print("Array with zeros moved ",rotated)