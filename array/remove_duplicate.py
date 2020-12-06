"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
LeetCode No.26
------------------------
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
80. Remove Duplicates from Sorted Array II
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums: list) -> int:
    slow = 0  # point to the last index of non-duplicates
    fast = 1
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            # print(nums,nums[fast],nums[slow])
            # remove the duplicate element
            slow += 1
            nums[slow] = nums[fast]

        fast += 1
    # print(nums)
    return slow + 1

def removeDuplicatesII(nums:list)->int:
    start = 0
    i = 1
    while i < len(nums):
        if nums[start]!=nums[i]: # not duplicated, update start and i
            start +=1
            i+=1
        elif i!=start+1:
            # not the first dupliacte number, then remove it from the list, no need to update index because
            # the length of the list has been shortened and the index i is pointing to the original next index
            nums.pop(i)
        else: # encounter the first duplicate number, update i
            i+=1
    return len(nums)