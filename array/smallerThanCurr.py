"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
No.1365
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
 That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.


https://leetcode.com/problems/count-of-smaller-numbers-after-self/
No.315
Counter of Smaller Numbers After self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]
"""


def smallerNumbersThanCurrent(nums: list) -> list:
    """
    Using bucket sort
    """
    buckets = [0] * 101
    for num in nums:
        buckets[num] += 1
    previous = 0
    for i, bucket in enumerate(buckets):
        if bucket != 0:
            buckets[i] = previous
            previous += bucket

    return [buckets[num] for num in nums]

def smallerThanCurr(nums:list) -> list:
    """
    Using dictionary
    """
    array = nums.copy()
    d={} # maps from value to the amount of number smaller than that
    nums.sort()
    for i in range(len(nums)):
        # since nums is already sorted, whatever before nums[i] are smaller than i
        if nums[i] not in d: # avoid counting the equal number as smaller
            d[nums[i]] = i
    for i in range(len(array)):
        array[i] = d[array[i]]
    return array

def smaller_self(nums:list)->list:
    """
    Traverse from the back of nums, and find the index to insert nums[i] to sorted_array such that it maintained sorted.
    The index of the sorted_array will be the amount of number that ae smaller than nums[i]
    if there are same number, insert it to the left, so that we won't count it as smaller
    """
    sorted_array = [] # always sorted
    count = []
    import bisect
    for i in range(len(nums)-1,-1,-1):
        index = bisect.bisect_left(sorted_array,nums[i]) # find the index to insert nums[i] into sorted_array
        sorted_array.insert(index,nums[i])
        count.append(index)
        #print('i',i,'count',count,'sorted',sorted_array)
    return count[::-1]

def merge_smallerself(nums:list)->list:
    """
    https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/445769/merge-sort-CLEAR-simple-EXPLANATION-with-EXAMPLES-O(n-lg-n)
    Use merge sort
    """

if __name__ == '__main__':
    nums = [8,1,2,2,3]
    # print(smallerNumbersThanCurrent(nums))
    # print(smallerThanCurr(nums))
    print(smaller_self(nums))