class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0

        for c in accounts:
            wealth = sum(c)
            richest = max(richest, wealth)
        
        return richest