'''
https://leetcode.com/problems/subsets/description/
No.78 Subsets
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
'''

def subSet(nums:list)->list:
    result = []
    backtrack(nums,result,[],0)
    return result

def backtrack(nums:list,result:list,curr:list,start:int):
    result.append(curr.copy())
    for i in range(start,len(nums)):
        curr.append(nums[i])
        backtrack(nums,result,curr,i+1)
        curr.pop()
