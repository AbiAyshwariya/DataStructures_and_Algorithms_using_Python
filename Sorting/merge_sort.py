class Solution:
    def mergesort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    n = len(arr)
    obj = Solution()
    obj.mergesort(arr, 0, n - 1)
    print("Sorted Array:", arr)
