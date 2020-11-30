'''
TwoSum problem:
Given an array of int and a target, return the pair of index that would sum to this target number.
Restriction: an element can only be used once
https://leetcode.com/problems/two-sum/
LeetCode No.1
'''

def twoSum_map(array:list,target:int)->list:
    d={}
    for i in range(len(array)):
        diff = target-array[i]
        if diff in d:
            return [i,d[diff]]
        d[array[i]]=i
    raise Exception("solution does not exit!")

def twoSum_pointer(array:list,target:int)->list:
    """
    This only works if array is distinct because we store the number : original index before sorted
    in a map, so if there's duplicated value the index get overwritten
    """
    if not array or len(array)<2: return[]
    d={}
    for i, nums in enumerate(array):d[nums]=i
    array.sort()
    head=0
    tail= len(array)-1
    while head<tail:
        sums=array[head]+array[tail]
        if sums==target:
            result = [d[array[head]],d[array[tail]]]
            result.sort()
            return result
        if sums<target:
            head+=1
        if sums>target:
            tail-=1
    raise Exception("solution does not exit!")

def twoSum_bs(numbers, target):
    """
    This only works if array is distinct
    """
    d = {}
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i, mid]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
    raise Exception("solution does not exit!")

def twoSum_bs_check(numbers, target):
    """
    This only works if the numbers is a distinct sorted array
    """
    investigatedSoFar = []
    for i in range(len(numbers)):
        if not numbers[i] in investigatedSoFar:
            investigatedSoFar.append(numbers[i])
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == tmp:
                    return([i + 1, mid + 1])
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
    raise Exception("solution does not exit!")



if __name__ == '__main__':
    l = [1,7,4,2,3,6]
    target=6
    print(twoSum_pointer(l,target))
    k = [1,2,3,4,67,90]
    print(twoSum_pointer(k,68))

