'''
https://leetcode.com/problems/combination-sum/description/
No.39 Combination Sum
Given a set of candidate numbers (candidates) ( without duplicates ) and a target number (target), find all
unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times .
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
-----------------------------------------
https://leetcode.com/problems/combination-sum-ii/
No.40 Combination Sum II
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''
def combinationSum(nums:list,target:int):
    result =[]
    backtrack(nums,result,[],target,0)
    pass

def backtrack(nums:list,solu:list,curr:list,remain:int,start:int):
    '''
    nums: global from combinationSum
    target: global from combinationSum
    solu: global, list contain the valid combinations
    curr: the current combination we are working with
    remain: the remained sum we are trying to match
    start: the start index of nums we are using
    '''
    if remain<0:return
    elif remain==0:
        solu.append(curr.copy())
    else:
        for i in range(start,len(nums)):
            curr.append(nums[i]) # try if we can find anything with nums[i]
            backtrack(nums,solu,curr,remain-nums[i],i)
            curr.pop()  # finish trying, remove it


def combinationSum2(nums:list,target:int):
    nums.sort()
    result=[]
    backtrack2(nums,result,[],target,0)


def backtrack2(nums:list,solu:list,curr:list,remain:int,start:int):
    '''
    nums: global from combinationSum
    target: global from combinationSum
    solu: global, list contain the valid combinations
    curr: the current combination we are working with
    remain: the remained sum we are trying to match
    start: the start index of nums we are using
    '''
    if remain==0:
        solu.append(curr.copy())
        return
    else:
        for i in range(start,len(nums)):
            # we always want to count the first element in the recursion even if it is the same as before
            # to avoid overcounting, we just ignore the duplicates after the first elmeent
            if i>start and nums[i]==nums[i-1]:
                continue
            if nums[i]>remain:
                break
            curr.append(nums[i]) # try if we can find anything with nums[i]
            # increment start with i+1 because we can only use an element once
            backtrack2(nums,solu,curr,remain-nums[i],i+1)
            curr.pop()  # finish trying, remove it