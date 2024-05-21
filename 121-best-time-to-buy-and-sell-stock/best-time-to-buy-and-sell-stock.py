class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # buy, sell = 0, 1
        # profit = 0
        # while sell < len(prices):
        #     if prices[sell] > prices[buy]:
        #         profit = max(profit, prices[sell] - prices[buy])
        #         sell+=1
        #     else:
        #         buy = sell
        #         sell+=1
        # return profit

        buy = 100001
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy

        return profit