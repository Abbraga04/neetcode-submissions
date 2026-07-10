class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        smallest = prices[0]

        for p in prices:
            best = max(best, p - smallest)
            smallest = min(smallest, p)

        return best


        
        

            
