class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Brute Force Solution
        # for item_index in range(0, len(prices)):
        #     item = prices[item_index]
        #     for forward_index in range(item_index+1, len(prices)):
        #         if item < prices[forward_index] and (prices[forward_index] - item) > profit:
        #             profit = prices[forward_index] - item

        # 2 Pointers approach
        first_pointer = 0
        second_pointer = 1

        while second_pointer < len(prices):
            if prices[first_pointer] < prices[second_pointer]:
                profit = prices[second_pointer] - prices[first_pointer]
                max_profit = max(max_profit, profit)
            else:
                first_pointer = second_pointer
            
            second_pointer += 1


        return max_profit