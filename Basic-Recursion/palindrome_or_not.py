import re


class Solution:
    def palindrome_or_not(self,s,i=0)->bool:
        s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        if i>=len(s)//2:
            return True
        if s[i]!=s[len(s)-i-1]:
            return False
        return self.palindrome_or_not(s,i+1)
obj=Solution()
print(obj.palindrome_or_not("malayalam",0))
print(obj.palindrome_or_not("madam",0))
print(obj.palindrome_or_not("Abi",0))
print(obj.palindrome_or_not("Abi Ayshwariya",0))
print(obj.palindrome_or_not("madsm",0))
