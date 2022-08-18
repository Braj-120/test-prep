class Solution:
    
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        count = 0
        dp = [999999999]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] > i:
                    continue
                if coins[j] == i:
                    dp[i] = 1
                else:
                    dp[i] =min(dp[i], dp[coins[j]] + dp[i-coins[j]])
            # print(dp)
        count = dp[amount]
        if count ==999999999:
            return -1
        return count

print(Solution().coinChange([1,2,5], 34))