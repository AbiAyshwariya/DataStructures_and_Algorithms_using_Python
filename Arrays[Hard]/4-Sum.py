class Solution:
    def four_sum(self, arr, target):
        n = len(arr)
        ans = []
        arr.sort()
        if n < 4:
            return ans

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    sum_ans = arr[i] + arr[j] + arr[k] + arr[l]

                    if sum_ans == target:
                        ans.append([arr[i], arr[j], arr[k], arr[l]])
                        k += 1
                        l -= 1
                        while k < l and arr[k] == arr[k - 1]:
                            k += 1
                        while k < l and arr[l] == arr[l + 1]:
                            l -= 1
                    elif sum_ans < target:
                        k += 1
                    else:
                        l -= 1

        return ans


# Example Usage
obj = Solution()
result_ans = obj.four_sum([1, 0, -1, -2, 2, 0], 0)
print("Quadruplets with given target sum are:", result_ans)



