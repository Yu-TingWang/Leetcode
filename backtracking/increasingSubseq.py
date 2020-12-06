'''
https://leetcode.com/problems/increasing-subsequences/
No.491 Increasing Subsequences
Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
and the length of an increasing subsequence should be at least 2.
'''

def findSubseq(nums:list)->list:
    result = []
    backtrack(nums,result,[],0)
    return result


def backtrack(nums,result,curr,index):
    if len(curr)>=2:
        result.append(curr.copy())
    used = set()
    for i in range(index,len(nums)):
        if len(curr) > 0 and curr[-1] > nums[i]: continue
        if nums[i] in used: continue
        curr.append(nums[i])
        used.add(nums[i])
        backtrack(nums,result,curr,i+1)
        curr.pop()