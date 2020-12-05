'''
https://leetcode.com/problems/target-sum/description/
No.494 Target Sum
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.
'''

def findTargetSumWays(nums:list,target:int):
    # states[i][0] = the number of ways that nums[:i+1] can make sum of -1000
    # states[i][1000] = the number of ways that nums[:i+1] can make sum of 0
    # states[i][2001] = the number of ways that nums[:i+1] can make sum of 1000
    states = [[0]*len(nums)]*2001
    return calculuate(nums,states,target)



def calculuate(nums:list,states,curr,target,i):
    if i == len(nums):
        if curr == target:
            return 1
        else:
            return 0
    else:
        if states[i][curr+1000] !=0:
            return states[i][curr+1000]
        subtract = calculuate(nums,states,curr+nums[i],target,i+1)
        add = calculuate(nums,states,curr-nums[i],target,i+1)
        states[i+1000] = add + subtract
        return states[i][curr+1000]