class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        min_val = prices[0]
        for val in prices[1:]:
            if val < min_val:
                min_val = val
            else:
                max_pro = max(max_pro, val-min_val)
        return max_pro
