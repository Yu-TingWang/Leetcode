'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
No.121 Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
No.122 Best Time to Buy and Sell Stock II
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
-------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
No.123 Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
def max_profitI(prices:list)->int:
    """
    only allows buy and sell once
    """
    min_val = sum(prices)
    max_profit = 0
    for i in range(len(prices)):
        min_val = min(min_val,prices[i])
        max_profit = max(max_profit,prices[i]-min_val)
    return max_profit

def max_profitII(price:list)->int:
    """
    allows multiple transaction, but can only hold one stock at a given time, namely, before buying a stock again,
    you must sell it out.
    the buying day will be the last continuous day that the price is smallest.
    Then, the selling day will be the last continuous day that the price is biggest.
    """
    i = profit = 0
    n = len(price)-1
    while i<n:
        while i< n and price[i+1] <= price[i]:
            i+=1
        buy = price[i]
        while i<n and price[i+1] > price[i]:
            i+=1
        sell = price[i]
        profit += sell - buy
    return profit

def max_profitII_dp(prices:list)->int:
    '''
    At a given day, there are three actions: buy, sell, or do nothing.
    '''
    lastBuy = -prices[0]
    lastSold = 0
    if len(prices)==0: return 0
    for i in range(1,len(prices)):
        print('i',i,'lb',lastBuy,'ls',lastSold,'prices[i]',prices[i])
        lastBuy = max(lastBuy,lastSold-prices[i])
        lastSold = max(lastSold,lastBuy+prices[i])
    return lastSold

if __name__ == "__main__":
    stocks = [7,1,5,3,6,4]
    #print(max_profitII(stocks))
    print(max_profitII_dp(stocks))
    s = [1,2,3,4,5,0]
    print(max_profitII(s))
