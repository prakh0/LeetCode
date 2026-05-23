class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            max_profit = max(max_profit,prices[i] - buy)
            buy = min(prices[i],buy)
        return max_profit
        