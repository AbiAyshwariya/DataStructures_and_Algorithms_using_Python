import math
class Solution:
    def switchsample(self,choice:int,arr)->int:
        if(choice==1):
            R=arr[0]
            result=math.pi*R*R
            return result
        elif(choice==2):
            L,B=arr[0],arr[1]
            result1=L*B
            return result1
        else:
            return -1


obj=Solution()
print(obj.switchsample(1,[5]))
print(obj.switchsample(2,[5,4]))

