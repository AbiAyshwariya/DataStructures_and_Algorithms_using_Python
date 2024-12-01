class Solution:
    def two_sum(self,arr,target):
        n=len(arr)
        map={}
        for i in range(n):
            complement=target-arr[i]
            if complement in map:
                return [map[complement],i]
            map[arr[i]] = i
        return []

obj=Solution()
result=obj.two_sum([2,5,6,8,11],14)
print("Array elements that sum upto to the given sum target:",result)