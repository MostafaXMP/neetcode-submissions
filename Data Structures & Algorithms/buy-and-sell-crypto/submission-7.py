class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumP = 0
        minimum = prices[0]
        for i in range(len(prices)):
            maximumP = max(maximumP, prices[i] - minimum)
            minimum = min(minimum, prices[i])
        return maximumP






