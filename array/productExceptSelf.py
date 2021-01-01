'''
https://leetcode.com/problems/product-of-array-except-self/
Leetcode No.238 Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of
space complexity analysis.)
'''
def productExceptSelf(nums:list)->list:
    product = 1
    result = []
    # assign result[i] with the value of product of all numbers come before i
    for i in range(len(nums)):
        result.append(product)
        product *= nums[i]
    product =1
    # times back the value of product of all numbers come after i
    for i in range(len(nums)-1,-1,-1):
        result[i] *= product
        product *= nums[i]
    return product