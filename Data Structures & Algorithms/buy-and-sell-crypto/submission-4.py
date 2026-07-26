class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maximum = max((prices[j] - prices[i]), maximum)

        return maximum
        