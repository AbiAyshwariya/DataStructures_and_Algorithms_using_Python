
class Solution:
    def subarray_count(self,arr,k):
        preffix_sum=0
        map={0:1}
        n=len(arr)
        cnt=0
        for num in arr:
            preffix_sum+=num
            abc=preffix_sum-k
            if abc in map:
                cnt+=map[abc]
            map[preffix_sum]=map.get(preffix_sum,0)+1
        return cnt
obj=Solution()
result=obj.subarray_count([1,2,3,-3,1,1,1,4,2,-3],3)
print("Count of the subarrays with the given sum is:",result)

