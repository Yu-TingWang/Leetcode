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
No.123 Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
-------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
No.188 Best Time to Buy and Sell Stock IV
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Notice that you may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).
-------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
No.714 Best Time to Buy and Sell Stock with Transaction Fee
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
'''
def max_profitI(prices:list)->int:
    """
    only allows buy and sell once
    """
    min_val = sum(prices) # initialize minimum with the biggest price
    max_profit = 0
    for i in range(len(prices)):
        min_val = min(min_val,prices[i])
        max_profit = max(max_profit,prices[i]-min_val)
    return max_profit

def max_profitII(price:list)->int:
    """
    allows multiple transaction, but can only hold one stock at a given time, namely, before buying a stock again,
    you must sell it out.
    """
    profit = 0
    i=0
    # since we can have unlimited transaction as long as we buy before sell,
    # if the previous price is lower then the next price, we should buy it and sell it.
    while i<len(price)-1:
        if price[i]<price[i+1]:
            profit +=price[i+1]-price[i]
        i+=1
    return profit


def max_profitII_dp(prices:list)->int:
    '''
    At a given day, there are three actions: buy, sell, or do nothing.
    '''
    # the buying day will be the last continuous day that the price is smallest.
    # Then, the selling day will be the last continuous day that the price is biggest.
    lastBuy = -prices[0] # buy stock[0]
    lastSold = 0
    if len(prices)==0: return 0
    for i in range(1,len(prices)):
        #print('i',i,'lb',lastBuy,'ls',lastSold,'prices[i]',prices[i])
        lastBuy = max(lastBuy,lastSold-prices[i]) # = max(skip,buy stock[i])
        lastSold = max(lastSold,lastBuy+prices[i]) # = max(skip, sell last buy stock at day[i])
    return lastSold

def max_profitIII(prices:list)->int:
    '''
    at most two transactions allowed.
    ++++++++ state transition ++++++++
    (i-1)th day     i-th day

            /       sell
    bought  \       skip (remain in bought state)

    (not holding stock in hand)
    no-state /      bought
             \      skip (remain in no state)

    sell    /       bought
            \       skip (remain in no state)
    '''
    pass

def max_profitIV(prices:list,k:int)->int:
    '''
    at most k transactions allowed
    '''
    pass

def max_profit_with_transaction(prices:list,fee:int)->int:
    '''
    allows multiple transaction, but can only hold one stock at a given time, namely, before buying a stock again,
    you must sell it out.
    However, each transaction has a transaction fee.
    '''
    pass

if __name__ == "__main__":
    stocks = [7,1,5,3,6,4]
    #print(max_profitII(stocks))
    print(max_profitII_dp(stocks))
    s = [1,2,3,4,5,0]
    print(max_profitII(s))
