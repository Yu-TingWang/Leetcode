'''
https://leetcode.com/problems/coin-change/description/
No.322 Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''
def coinChange(coins:list,amount:int):
    states=[0] +[float('inf')]*amount # states[i] = the fewest number of coins to make up to i
    # states[i] = min(states[j])+1 where j = i - {coin for coin in coins}
    coins.sort()
    for i in range(len(states)):
        for j in range(len(coins)):
            if coins[j]<=i and states[i-coins[j]]!=float('inf'):
                print('true;',end="")
                # since we have states[0] = 0 -> when i = coins[j] -> i-coins[j] = 0
                # -> states[coins[j]] = 1
                states[i] = min(states[i],1+states[i-coins[j]])
            print('i',i,'j',(j,coins[j]),states)
    return -1 if not states[amount] else states[amount]


if __name__ == '__main__':
    coins= [1,2,5]
    amount = 11
    print(coinChange(coins,amount))




