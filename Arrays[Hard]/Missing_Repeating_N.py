class Solution:
    def missing_repeating(self,arr,):
        n=len(arr)
        s=0
        s2=0
        Sn=(n*(n+1))//2
        S2n=(n*(n+1)*(2*n+1))//6
        for i in range(n):
            s+=arr[i]
            s2+=arr[i]*arr[i]
        val1=s-Sn
        val2=s2-S2n
        val2=val2//val1
        x=(val1+val2)//2
        y=x-val1
        return [x,y]
obj=Solution()
result=obj.missing_repeating([4,3,6,2,1,1])
print("Missing and Repeating elements in the array are: ",result)