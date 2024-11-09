class Solution:
    def datatypes(self,str):
        if str=="Character":
            return 1
        elif str=="Integer" or str=="Float":
            return 4
        elif str=="Long" or str=="Double":
            return 8
        else:
            return -1
        
obj=Solution()
print(obj.datatypes("Integer"))
print(obj.datatypes("Character"))
print(obj.datatypes("Float"))
print(obj.datatypes("Double"))
