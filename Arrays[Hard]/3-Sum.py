class Solution:
    def three_sum(self, arr):
        ans = []
        arr.sort()
        n = len(arr)

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            j, k = i + 1, n - 1

            while j < k:
                sum_ans = arr[i] + arr[j] + arr[k]

                if sum_ans < 0:
                    j += 1
                elif sum_ans > 0:
                    k -= 1
                else:
                    # Add the triplet to the answer list
                    ans.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1

                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1

        return ans

obj = Solution()
result = obj.three_sum([-1, 0, 1, 2, -1, -4])
print("Triplets with sum as 0:", result)
