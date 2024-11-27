class Solution:
    def quicksort(self,arr,low,high):
        if low<high:
            partition=self.f(arr,low,high)
            self.quicksort(arr,low,partition-1)
            self.quicksort(arr,partition+1,high)
        return arr

    def f(self,arr,low,high):
        pivot=arr[low]
        i,j=low+1,high
        while True:
            while arr[i]<=pivot and i<=high:
                i+=1
            while arr[j]>pivot and j>=low:
                j-=1
            if(i>=j):
                break
            arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j

if __name__ == "__main__":
    arr=[45,76,87,85,1,2,4,2,54,9]
    high=len(arr)
    low=0
    obj=Solution()
    obj.quicksort(arr,low,high-1)
    print("Sorted Array: ",arr)

