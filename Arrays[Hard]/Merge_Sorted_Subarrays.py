class Solution:
    def merge_sorted_arrays(self, arr1, arr2, m, n):
        arr1.extend([0] * n)
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1
        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
        return arr1

obj=Solution()
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
result=obj.merge_sorted_arrays(arr1,arr2,len(arr1),len(arr2))
print("Merged and Sorted Array : ",result)

