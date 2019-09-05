"""
Solution 1:
Idea comes from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/

The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm.

Here, the logic is to calculate the difference (max_cur + prices[i] - prices[i-1]) of the original array, 
and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.

           [7,1,5,3,6,4]
ma_cur:    [0,0,4,2,5,3] (reset the total difference to 0 if it falls below 0)
ma_so_far: [0,0,4,4,5,5]

Solution 2:
We calculate the min_price before prices[i], then the max profit if we sell the stock on day i is (prices[i] - min_price).

"""

# Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cur, max_so_far = 0, 0 
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur + prices[i]- prices[i-1])
            max_so_far = max(max_so_far, max_cur)
        return max_so_far

# Solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max(0, max_profit)
