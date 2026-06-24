class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        for i in range(len(prices)):
            tempSum = 0
            r = i + 1
            while r < len(prices):
                if prices[r] - prices[i] > tempSum:
                    tempSum = prices[r] - prices[i]
                r += 1
            if tempSum > res:
                res = tempSum

        return res
                    
                
            
            