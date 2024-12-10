class Solution:
    def generate(self,numRow):
        ans=[]
        for row in range(1,numRow+1):
            ansRow=[]
            ans_num=1
            for col in range(1,row+1):
                ansRow.append(ans_num)
                ans_num=ans_num*(row-col)//col
            ans.append(ansRow)
        return ans
obj=Solution()
result=obj.generate(5)
print("Pascals triangle is as follows: ",result)