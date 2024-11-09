#In Python immutable datatypes such as String, Integer and Tuple behaves like they are passed by value
#In Python mutable datatypes such as List and Dictionaries behaves like they are passed by reference
class Solution:
    def pass_by_value_or_reference(self, a,lst):
        a+=1
        lst[0]+=2
        return a,lst[0]
userinput=input("Enter the value separated by space: ")
num,new_num=map(int,userinput.split())
obj=Solution()
print(obj.pass_by_value_or_reference(num,[new_num]))





