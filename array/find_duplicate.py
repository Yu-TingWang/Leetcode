"""
LeetCode No.287
"""
def findDuplicates(nums:list)->int:
    """
    O(n) time, no extra space
    Approach: Take advantage the property that nums only contains positive integers.
    Negate the element if its index as been visited, so when we encounter a negative number,
    it must be duplicated.
    :param nums: list[int], which contains n+1 integers from [1,n]
    :return: the duplicate number
    """
    # find the
    for i in range(len(nums)):
        if nums[abs(nums[i])]<0:
            return abs(nums[i])
        else:
            nums[abs(nums[i])] = - nums[abs(nums[i])]
