'''
https://leetcode.com/problems/delete-and-earn/description/
No.740. Delete and Earn
Given an array nums of integers, you can perform operations on the array.
In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
You start with 0 points. Return the maximum number of points you can earn by applying such operations.
'''

def deleteAndEarn(nums:list)->int:
    '''

    '''
    from collections import Counter
    count = Counter(nums) # maps from the number to its frequency in nums
    # states[i] the max of pick/delete all numbers in nums ≤ i
    states=[0]*10000 # since nums[i] is in [1,10000]
    # there are two outcome for i: i is being picked -> then states[i] = count[i]*i + states[i-2]
    # i is deleted : states[i] = states[i-1]. we take the max of the two
    states[1] = count[1]
    for i in range(2,len(nums)-1):
        states[i] = max(states[i-1],count[i]*i+states[i-2])
    return states[-1]
