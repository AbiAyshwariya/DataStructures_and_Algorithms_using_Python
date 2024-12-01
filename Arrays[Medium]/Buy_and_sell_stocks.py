class Solution:
    def buy_and_cell_stocks(self,prices):
        n=len(prices)
        profit=0
        mini=prices[0]
        for i in range(n):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit
obj=Solution()
result=obj.buy_and_cell_stocks([7,1,5,3,6,4])
print("Maximum Buying and Selling Profit is:",result)