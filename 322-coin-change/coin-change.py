class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000000000]*(amount+1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(1,len(dp)):
            if dp[i] == 1:
                continue
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] == 10000000000:
            return -1
        return dp[amount]