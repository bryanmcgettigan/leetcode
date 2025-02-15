class Solution:
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        current =prices[0]
        PriceLength= len(prices)
        if PriceLength==1:
            return 0
        for index in range(1,PriceLength):
            print(index)
        for index in range(1,len(prices)):
            print(index)
            #best = max(prices[index+1]-current,best)
            #current=min(current,prices[index+1])

        return best

solution = Solution()

prices =[1,2]

print(solution.maxProfit(prices))