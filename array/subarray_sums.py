"""
Given an array of integers and an integer k, return the total number of continuous subarrays whose sum equals to k.

https://leetcode.com/problems/subarray-sum-equals-k/
LeetCode No.560
"""

def subarraySum(array:list,k:int)->int:
    """
    :param array:list[int]
    :param k: int, the target sum
    :return: int, the amount of continuous subarray who sums to k.
    """
    cum=0
    total=0



def subarray_sum(nums: list, k: int) -> int:
    """
    O(n^2) time, O(n) space.
    :param nums: list[int],
    :param k: int, the target sum
    :return: int, the amount of continuous subarray who sums to k.
    """
    # construct a cumulativeSum array | cum[i] = sum(nums[:i])
    if not nums:return 0
    total=0
    cum=[0] # if start from the begining of the list, diff = cum[i]-cum[0]
    for i in range(len(nums)):
        cum.append(cum[i]+nums[i])
    for i in range(len(cum)-1):
        for j in range(i+1,len(cum)):
            if cum[j]-cum[i]==k:
                total+=1
    return total