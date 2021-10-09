class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimal = prices[0]
        maximal = 0
        for element in prices:
            maximal = max(maximal, element-minimal)
            if element < minimal:
                minimal = element
        return maximal

# EOF #
