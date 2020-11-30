"""
https://leetcode.com/problems/longest-increasing-subsequence/
LeetCode num.300
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]

LIS : Longest Increasing Subsequence

LeetCode num.673
Find the number of LIS
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""


def lengthofLIS(nums: list) -> int:
    states = [1] * len(nums)
    # states[i] is the length of the longest increasing subsequence that ends at nums[i]
    # i.e. states[i] = max(states[j]+1) for all j<i
    for i in range(1, len(nums)):
        # why i starts with 1? because states[0] can only be 1, so no need to traverse i=0
        for j in range(i):
            if nums[j] < nums[i]:
                states[i] = max(states[i], states[j] + 1)
                # why states[j] +1 ?
                # states[j] represents the amount of numbers that are smaller than nums[j]
                # these numbers are guaranteed strictly increasing because if x<y and y<z , then x<z is guaranteed
                # the +1 is nums[j] itself
            # print('j:',j,',i:',i, ',states', states)
    return max(states)


def numofLIS(nums: list) -> int:
    lis = [1] * len(nums)  # lis[i] is the length of LIS that ends at nums[i]
    count = [1] * len(nums)  # count[i] is the number of LIS that ends at nums[i]
    total = 0  # the current number of LIS at nums[:i]
    max_len = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if lis[i] == lis[j] + 1:
                    count[i] += count[j]
                    print('if','i',i,'j',j,'lis',lis,'count',count)
                elif lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    count[i] = count[j]
                    print('elif','i',i,'j',j,'lis',lis,'count',count)
        if max_len == lis[i]:
            total += count[i]
        elif max_len < lis[i]:
            max_len = lis[i]
            total = count[i]
    print(lis)
    print(count)
    return total


def buggynumofLIS(nums: list) -> int:
    # this method will not work
    # try nums = [1,3,5,4,7], The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
    # but by using this approach it will produce states as [1,2,3,3,4]
    states = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                states[i] = max(states[i], j + 1)
    max_len = max(states)
    return states.count(max_len)


if __name__ == '__main__':
    # l = [10,9,2,5,3,7,101,18]
    # print(l)
    # print(lengthofLIS(l))
    # l = [2,2,2,2,2]
    # print(l)
    # print(lengthofLIS(l))
    # print(numofLIS(l))
    l = [1, 3, 5, 4, 7]
    print(lengthofLIS(l))
    print(numofLIS(l))
