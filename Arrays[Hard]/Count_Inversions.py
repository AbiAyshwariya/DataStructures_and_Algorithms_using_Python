class Solution:
    def inversionCount(self, arr):
        def merge(arr, temp_arr, left, mid, right):
            i = left
            j = mid + 1
            k = left
            inv_count = 0
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
            return inv_count

        def mergeSort(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += mergeSort(arr, temp_arr, left, mid)
                inv_count += mergeSort(arr, temp_arr, mid + 1, right)
                inv_count += merge(arr, temp_arr, left, mid, right)
            return inv_count

        temp_arr = [0] * len(arr)
        return mergeSort(arr, temp_arr, 0, len(arr) - 1)

obj = Solution()
result = obj.inversionCount([5, 3, 2, 4, 1])
print("Number of Inversions are:", result)
