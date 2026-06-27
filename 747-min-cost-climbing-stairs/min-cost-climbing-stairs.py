class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            ans1 = helper(i+1)
            ans2 = helper(i+2)
            dp[i] = cost[i] + min(ans1, ans2)
            return dp[i]

        dp = [-1] * len(cost)
        return min(helper(0), helper(1))