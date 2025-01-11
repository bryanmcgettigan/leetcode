def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    hash_table = {}
    maxProfit =0
    cheapestPrice=max(prices)
    for index,num in enumerate(prices[:-1]):
        if(index>=0 and num<cheapestPrice):
            cheapestPrice=num
        if(prices[index+1]-cheapestPrice>maxProfit):
            maxProfit=prices[index+1]-cheapestPrice
        


    return maxProfit
        
prices = [7,1,5,3,6,4]

print(maxProfit(prices))