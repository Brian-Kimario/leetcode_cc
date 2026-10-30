class Solution(object):
    def coinChange(self, coins, amount):
        # Create a DP array filled with a float('inf') or amount + 1 as a placeholder for infinity
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Iterate through all amounts from 1 up to the target amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # If the amount is still filled with the placeholder, it's unreachable
        return dp[amount] if dp[amount] <= amount else -1
        