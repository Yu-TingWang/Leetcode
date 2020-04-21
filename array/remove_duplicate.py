"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
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