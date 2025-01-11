def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    baseProfit =0
    for index,num in enumerate(prices):
            for numtwo in prices[index+1:]:
                  profit=numtwo-num
                  if(profit>baseProfit):
                        baseProfit=profit

    return baseProfit
        

prices = [7,1,5,3,6,4]

print(maxProfit(prices))