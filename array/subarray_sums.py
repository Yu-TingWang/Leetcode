"""
Given an array of integers and an integer k, return the total number of continuous subarrays whose sum equals to k.

l is a subarray of A if l = A[i:j]

https://leetcode.com/problems/subarray-sum-equals-k/
LeetCode No.560
Given a list of non-negative numbers and a target integer k, write a function to check
if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is,
sums up to n*k where n is also an integer.
-----------------

LeetCode No.523. Continuous Subarray Sum
"""
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

def subarraySum(array:list,k:int)->int:
    """
    Construct a dictionary that maps from continuous sum to its amount
    Time : O(n)
    Space~ O(n)
    :param array:list[int]
    :param k: int, the target sum
    :return: int, the amount of continuous subarray who sums to k.
    """
    curr_sum=0
    total=0
    from collections import defaultdict
    d = defaultdict(lambda:0) # maps from subarray_sum to its amount in array
    d[0]=1 # array[:0] = 0 , there's one 0
    for i in range(len(array)):
        curr_sum += array[i]
        if (curr_sum - k) in d:
            # if the difference between curr_sum and target is in map, then the subarray from index i to the index j has the differnece
            # sum(array[i:j+1]) will equate to k
            total += d[curr_sum-k]
        d[curr_sum]+=1
    return total


def subK(array,k)->int:
    """
    First, we traverse the list once, change the element into the modulus of k
    """
    k = abs(k)
    if k == 0:
        return any(array[i]==array[i+1]==0 for i in range(len(array)-1))
    d = {0:-1} # since 0 is a multiple of anything, put it to map, if in the iteration we encounter subarray at least 2
    # that sums up to 0, we should return true
    # maps from mod to its amount
    curr_mod_sums = 0
    for i,num in enumerate(array):
        print('i',i,'d',d,curr_mod_sums)
        curr_mod_sums = (curr_mod_sums+num)%k
        if curr_mod_sums not in d :
            d[curr_mod_sums] = i
        elif i - d[curr_mod_sums] >1:
            print('i',i,'curr',curr_mod_sums)
            return True
    print(d)
    return False

if __name__ == '__main__':
    l = [3,4,7,2,-3,1,4,2]
    #print(subarraySum(l,7))
    k = [23,2,4,6,7]
    print(subK(k,6))
    p = [22,4,6,7,9]
    print(subK(p,15))
    h = [0,0]
    print(subK(h,-1))
