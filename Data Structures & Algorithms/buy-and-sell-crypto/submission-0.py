class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for item_index in range(0, len(prices)):
            item = prices[item_index]
            for forward_index in range(item_index+1, len(prices)):
                if item < prices[forward_index] and (prices[forward_index] - item) > profit:
                    profit = prices[forward_index] - item
        
        return profit