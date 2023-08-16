

class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        result = 0
        leng = len(prices)

        while right < leng:
            if prices[left] > prices[right]:
                left = right
                
            else :
                # 뺀 값
                result = max(prices[right] - prices[left], result)
            right += 1
        
        return result
        """
        :type prices: List[int]
        :rtype: int
        """