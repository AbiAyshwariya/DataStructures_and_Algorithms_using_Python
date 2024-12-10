class Solution:
    def findFloor(self, arr, n, x):
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def findCeil(self, arr, n, x):
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def getFloorAndCeil(self, arr, n, x):
        arr.sort()  
        f = self.findFloor(arr, n, x)
        c = self.findCeil(arr, n, x)
        return (f, c)


obj = Solution()
result = obj.getFloorAndCeil([1, 2, 8, 10, 10, 12, 19], 7, 5)
print("Floor and Ceil are:", result)
