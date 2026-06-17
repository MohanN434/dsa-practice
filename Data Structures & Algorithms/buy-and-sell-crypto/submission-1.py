class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit, left = 0, 0

        for right in range(left + 1, len(prices)):
            currentProfit = prices[right] - prices[left]
            totalProfit = max(currentProfit, totalProfit)

            if prices[right] < prices[left]:
                left = right

        return totalProfit
