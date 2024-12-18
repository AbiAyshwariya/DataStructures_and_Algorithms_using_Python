class Solution:
    def next_permutation(self,arr):
        n=len(arr)
        ind=-1
        for i in range(n-2,-2,-2):
            if arr[i]<arr[i+1]:
                ind=i
                break
        if ind==-1:
            arr.reverse()
            return arr
        for i in range(n-1,ind,-1):
            if arr[i]>arr[ind]:
                arr[ind],arr[i]=arr[i],arr[ind]
                break
        arr[ind+1:]=reversed(arr[ind+1:])
        return arr
obj=Solution()
result=obj.next_permutation([2,1,5,4,3,0,0])
print("Next immediate permutation is : ",result)