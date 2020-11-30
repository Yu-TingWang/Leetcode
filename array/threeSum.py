"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero .
Restriction: The solution set must not contain duplicate triplets

https://leetcode.com/problems/3sum/
LeetCode No.15

https://leetcode.com/problems/3sum-closest/
LeetCode No.16
"""


def threeSum_map(array: list, target):
    result = []
    d = {}
    # construct a dictionary that maps from value to its index
    for i, num in enumerate(array):  d[num] = i
    array.sort()  # O(nlogn)
    #  this is for checking the duplicate
    check = set()
    for i in range(len(array)):  # O(n)
        # print(check)
        for j in range(i+1, len(array)):  # O(n)
            diff = target - array[i] - array[j]
            # print(i,j)
            if (diff in d) and (d[diff] > j) and ((array[i],array[j]) not in check):  # O(1)
                result.append((array[i], array[j], diff))
                check.add((array[i],array[j]))

    # the above loop takes O(n^2)
    return result


def threeSum_pointer(array: list, target):
    array.sort()  # O(nlogn)
    result = []
    n = len(array)
    print(array)
    for i in range(n - 2):  # O(n)
        # The last two , if are one of ThreeSum, must be the array[r], so no need to take it as array[i]
        # array[i] is the smallest among the triplets
        if array[i] > target:  # then its impossible to find other two elements
            break
        if i > 0 and array[i] == array[i - 1]:  # skip to next iteration: adjust the index to the next diff number
            continue
        l = i + 1  # since [:i] has been tried
        r = n - 1
        while l < r:  # ~O(n)
            total = array[i] + array[l] + array[r]
            if total < target:  # need to make the sum bigger
                l += 1
            elif total > target:  # need to make the sum smaller
                r -= 1
            else:  # then this tuple is the threeSum
                result.append([array[i], array[l], array[r]])
                # adjust the left pointer to the next diff number
                while l < r and array[l] == array[l + 1]:
                    l += 1
                # adjust the right pointer to the next diff number
                while l < r and array[r] == array[r - 1]:
                    r -= 1
                print('i',i,'l',l,'r',r)
                l += 1 # why update again ? because it array[l]!=array[l+1] whe exit the loop, so we need to get the 'l+1'
                r -= 1
        # the above loop takes O(n^2)
    return result

def threeSum_closet(array:list,target:int)->int:
    array.sort()
    n=len(array)
    result=sum(array[n-3:])
    for i in range(n-2):
        start , end = i+1, n-1
        while start<end:
            sums = array[i]+array[start]+array[end]
            if abs(sums-target)<abs(result-target):
                result=sums
            if sums>target:
                end-=1
            else:
                start+=1
    return result

if __name__ == "__main__":
    array=[-1,0,1,2,-1,-4]
    #print(threeSum_map(array,0))
    #print(threeSum_pointer(array,0))
    print(threeSum_closet(array,6))