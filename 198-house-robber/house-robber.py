class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            robCurrent = nums[i] + helper(i+2)
            skipCurrent = helper(i+1)
            dp[i] = max(robCurrent, skipCurrent)
            return dp[i]
        dp = [-1] * (len(nums) + 1)
        return helper(0)      

