"""
https://leetcode.com/problems/valid-triangle-number/
No.661 Valid Triangle Number
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.
"""

def triangleNumber(nums:list)->int:
    if len(nums) < 3:
        return 0
    result = 0
    for i in range(2,len(nums)):
        left = 0
        right = i-1
        while right > left:
            if nums[left]+nums[right]> nums[i]:
                # if nums[left] is big enough to construct triangle, then nums[left+1:right] is even bigger,
                # so they must qualify. hence we add |nums[left:right]|
                result += right -left
                right -=1 # decrement right until right is too small to construct triangle
            else:
                left +=1 # increment left until left is big enough to construct triangle
    return result


if __name__ == '__main__':
    l = [2,2,3,4]
    print(triangleNumber(l))
