class Solution:
    def reverse_an_array(self,arr,left=0,right=None):
        if right is None:
            right=len(arr)-1
        if left>=right:
            return arr
        arr[left],arr[right]=arr[right],arr[left]
        return self.reverse_an_array(arr,left+1,right-1)
obj=Solution()
print(obj.reverse_an_array([1,2,3,4,5],0))
print(obj.reverse_an_array(["Abi","Ayshu","Ayshwariya","Riya"],0))
