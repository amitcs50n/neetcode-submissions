class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy + 1, len(prices)):
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit, profit)
        
        # return max_profit

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit




        