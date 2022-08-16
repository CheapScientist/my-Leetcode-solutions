// https://leetcode.com/problems/coin-change-2

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]