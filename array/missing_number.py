"""
Given an unsorted array, find the missing number.

https://leetcode.com/problems/missing-number/
LeetCode No.268

https://leetcode.com/problems/first-missing-positive/description/
LeetCode No.41

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
LeetCode No.448
"""

def missingNumber(nums:list)->int:
    """ No.268
    A mathematical approach
    :param nums: list[int], contains n distinct numbers from 0 to n.
    :return: The missing number from the list
    """
    n=len(nums)
    return n*(n+1)//2-sum(nums)

def missing_number(nums:list)->int:
    """ No.268
    Run in linear time complexity, and constant extra space complexity.
    :param nums: list[int], contains n distinct numbers from 0 to n.
    :return: The missing number from the list
    """
    # take advantage of the overlap with the index and the number
    for i in range(len(nums)):
        if nums[nums[i]]<0:
            return nums[i]
        else:
            nums[nums[i]]=-1

def missing_positive(nums:list)->int:
    """ No.41
    Run in linear time complexity, ~O(n) space .
    :param nums: list[int], unsorted array.
    :return: the smallest missing positive integer.
    """
    prev = 1
    n = len(nums)
    i = 0
    num = set(nums)
    while prev in num and i < n:
        prev += 1
        i += 1
    return prev


def first_missing_positive(nums:list)->int:
    """ No.41
    Run in O(n) time, O(1) space.
    Approach: Modify the array as a hash function | each index corresponding to the frequency of the number
    abd the original number. After finish modifying, check which index corresponds to frequency=0.
    :param nums: list[int] , unsorted array
    :return: the smallest missing positive integer.
    """
    nums.append(0) # hash function is used to check if an index (0...n-1) has been used or not.
    # if we dont append 0, it will always return 0 as the answer
    n = len(nums)
    for i in range(n): # filter
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(n):
        # use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
        # num[i]%n will get original number
        # num[i] // n will get the frequency of the number i
    for i in range(1, len(nums)):
        if nums[i] // n == 0:
            return i
    return n


def missing_first_positive(nums:list)->int:
    """ No.41
    Run in O(n) time, O(1) space
    Approach: filter negative and >= len(nums), then move the element to its index
    ex. move 1 to nums[0], after traverse the whole list, traverse from the beginning of the list and
    check if the element corresponds to its index.
    :param nums: list[int], unsorted array.
    :return: the smallest missing positive integer.
    """
    n = len(nums)
    for i in range(n):
        ## why use a while loop not simly a if statement? cuz one swap might not be enough
        # skip the negative and those greater than length
        # move the element to its index ( ex. move 1 to nums[0])
        while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            temp = nums[i]
            nums[i] = nums[nums[i]-1]
            nums[nums[i]-1]=temp
    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    # if not yet return, then the list contains all number from [1,n]
    return n+1


def disappeared_numbers(nums: list) -> list:
    """ No.448
    Approach: Move the element to its corresponding index ex. move 1 to nums[0]
    After finish traversing for the first time, return whomever number does not correspond to index
    :param nums: list[int], where each element [1:len(n)]
    :return: list[int], the numbers from [1:len(n)] not in nums
    """
    for i in range(len(nums)):
        if nums[i] != i + 1:
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
    return [i + 1 for i, num in enumerate(nums) if num != i + 1]


def find_disappeared_numbers(nums:list)->list:
    """ No.448
    Approach: Take advantage of the overlap with the element and the index.
    when encounter a number, uses it as index and negate the element pointed by it
    to mark as visited. At the end of iteration, those who remained positive are disappeared.
    :param nums: list[int], where each element [1:len(n)]
    :return: list[int] , the numbers from [1:len(n)] not in nums
    """
    for i in range(len(nums)):
        index = abs(nums[i])
        nums[index] = -abs(nums[index])

    return [i+1 for i,num in enumerate(nums) if num>0]


if __name__ == "__main__":
    array=[4,3,2,7,8,2,3,1]
    print(disappeared_numbers(array))