class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        
        while len(dp) < n + 1:
            dp.append(dp[-1] + dp[-2])
        return dp[n]