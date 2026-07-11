class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # for every num check if the current is bigger than prev and then see if the differnce is more
        left = 0
        right = 1
        curr = 0
        while len(prices)> right:
            if prices[right] - prices[left] < 0:
                left = right
                right += 1
            else:
                if prices[right] - prices[left] > curr:
                    curr = prices[right] -prices[left]
                right += 1
        return curr
        # 3, 0, 2, 5, 1
            


        