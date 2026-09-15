class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyp = 1000
        maxp = 0

        for p in prices:
            if p < buyp:
                buyp = p
            else:
                maxp = max(maxp,p-buyp)

        return maxp