"""
https://leetcode.com/problems/maximum-subarray/
No.53
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
def maxSubarray(nums:list)->int:
    states = [nums[0]]*len(nums)
    # states[i] = the sum of maxSubarry the ends at nums[i]
    curr_max = nums[0]
    for i in range(1,len(nums)):
        states[i] = max(states[i-1]+nums[i],nums[i])
        curr_max = max(curr_max,states[i])
    return curr_max


def maxSub_divideConquer(nums:list)->int:
    """
    Divide-and-conquer method.
    The maximum summation of subarray can only exists under following conditions:
    1. the maximum summation of subarray exists in left half.
    2. the maximum summation of subarray exists in right half.
    3. the maximum summation of subarray exists crossing the midpoints to left and right.
    1 and 2 can be reached by using recursive calls to left half and right half of the subarraies.
    Condition 3 can be found starting from the middle point to the left,
    then starting from the middle point to the right. Then adds up these two parts and return.

    T(n) = 2*T(n/2) + O(n)
    this program runs in O(nlogn) time
    """
    maxsum = subArray(nums,0,len(nums)-1)
    return maxsum

def subArray(nums:list,left:int,right:int):
    if left==right:
        return nums[left]
    mid = left + (right-left)//2
    leftSum = subArray(nums,left,mid) # left part of the subarray sum
    rightSum = subArray(nums,mid+1,mid) # right part of the subarray sum
    midSum = subArray(nums,left,mid,right) # cross part of the subarray sum
    if leftSum >=rightSum and leftSum>=midSum:
        return leftSum
    if rightSum >=leftSum and rightSum >=midSum:
        return rightSum
    return midSum

def midSubArray(nums:list,left:int,mid:int,right:int):
    leftsum = float('-inf')
    rightsum = float('-inf')
    sums=0
    for i in range(mid,left-1,-1):
        sums+=nums[i]
        if leftsum < sums:
            leftsum = sums
    sums=0
    for j in range(mid+1,right+1):
        sums+=nums[j]
        if rightsum < sums:
            rightsum = sums
    return leftsum+rightsum



if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubarray(nums))

