class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000000000]*(amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1,len(dp)):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] == 10000000000:
            return -1
        return dp[amount]