class Solution:
    def check_plaindrome(self,n)->bool:
        original=n
        reverse_num=0
        while(n>0):
            rem = n%10
            reverse_num=reverse_num*10+rem
            n=n//10
        if(reverse_num==original):
            return True
        else:
            return False

obj=Solution()
print(obj.check_plaindrome(179971))
print(obj.check_plaindrome(121))
print(obj.check_plaindrome(345))