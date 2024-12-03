class Solution:
    def consecutive_sequence(self,arr):
        n=len(arr)
        if n==0:
            return 0
        longest=1
        st=set()
        for i in range(n):
            st.add(arr[i])
        for it in st:
            if it-1 not in st:
                cnt=1
                x=it
                while x+1 in st:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)
        return longest
obj=Solution()
result=obj.consecutive_sequence([101,102,100,101,101,4,3,2,3,2,1,1,1,2])
print("Length of Longest consecutive subsequence in the array is: ",result)
