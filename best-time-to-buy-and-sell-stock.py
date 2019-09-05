class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float('inf')
        
        profit = float('-inf')
        for i in range(len(prices)):
            if profit < prices[i] - currMin:
                profit = prices[i] - currMin

            currMin = min(currMin, prices[i])

        return profit if profit > 0 else 0
