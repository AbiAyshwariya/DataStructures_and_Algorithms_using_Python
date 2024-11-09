class Solution:
    def reverse(self,x):
        INT_MIN,INT_MAX=-2**31,2**31-1
        sign=-1 if x<0 else 1
        reverse=int(str(abs(x))[::-1])*sign
        if reverse<INT_MIN or reverse>INT_MAX:
            return 0
        return reverse

obj=Solution()
print(obj.reverse(321))
print(obj.reverse(-756))
print(obj.reverse(210))
