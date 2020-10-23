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
    if not array or len(array)<2: return[]
    array.sort()
    head=0
    tail= len(array)-1
    while head<tail:
        sums=array[head]+array[tail]
        if sums==target:
            return[head,tail]
        if sums<target:
            head+=1
        if sums>target:
            tail-=1
    raise Exception("solution does not exit!")

def twoSum_bs(numbers, target):
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
    raise Exception("solution does not exit!")

def twoSum_bs_check(numbers, target):
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





