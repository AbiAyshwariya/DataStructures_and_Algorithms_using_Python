class Solution:
    def reversePairs(self, arr):
        def merge(arr, temp_arr, left, mid, right):
            i = left
            j = mid + 1
            k = left
            reverse_count = 0

            for i in range(left, mid + 1):
                while j <= right and arr[i] > 2 * arr[j]:
                    j += 1
                reverse_count += (j - (mid + 1))

            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
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

            return reverse_count

        def mergeSort(arr, temp_arr, left, right):
            reverse_count = 0
            if left < right:
                mid = (left + right) // 2
                reverse_count += mergeSort(arr, temp_arr, left, mid)
                reverse_count += mergeSort(arr, temp_arr, mid + 1, right)
                reverse_count += merge(arr, temp_arr, left, mid, right)
            return reverse_count

        temp_arr = [0] * len(arr)
        return mergeSort(arr, temp_arr, 0, len(arr) - 1)

obj = Solution()
result = obj.reversePairs([1, 3, 2, 3, 1])
print("Number of Reverse Pairs are:", result)
