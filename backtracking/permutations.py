'''
https://leetcode.com/problems/permutations/description/
No.46 Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
---------------------
No.46
Given an array nums of non-distinct integers, return all the possible permutations. You can return the answer in any order.
'''
def permute(nums:list):
    result = []
    backtrack(nums,[],[])
    return result

def backtrack(nums,result,curr):
    '''
    nums, list[int] global from permute
    result, list[list[int]], global
    curr, list[int] current list we are working at
    '''
    if len(curr)==len(nums):
        result.append(curr.copy())
    else:
        for i in range(len(nums)):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            backtrack(nums,result,curr)
            curr.pop()