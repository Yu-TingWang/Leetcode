'''
https://leetcode.com/problems/maximum-width-ramp/
No.962
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.
Find the maximum width of a ramp in A.  If one doesn't exist, return 0.
'''

def maxWidthRamp_2ptr(array:list)->int:
    """
    First, we compute a list max_right, where max_right[i] = max(array[:i]). The purpose of creating it is to eliminate
    unnecessary comparison. ex, for [6,0,8,1,5], when we get 0,5 we don't have to compare anything between them since
    nothing between them will produce widthRamp longer than theirs.
    Then, we will use two pointers to track.
    right pointer: iterate the max_right array
    left pointer: iterate the original array
    """
    max_right=[array[-1]]*len(array)
    for i in range(len(array)-2,-1,-1):
        max_right[i] = max(max_right[i+1],array[i])
    print(max_right)
    # max_right[i] = max(array[i:])
    left = right = result = 0
    while right< len(array):
        print('right',right,array[right],'left',left,array[left])
        while left<right and array[left] > max_right[right]:
            print('enter loop')
            left +=1
        result = max(result,right-left)
        right +=1
    return result



def maxWidthRamp_stack(array:list)->int:
    """
    keep a stack of decreasing order elements.
    [6,0,8,2,1,5]
    Decreasing order stack : 6,0.
    No need to push 8 to stack. Why ? because whoever greater than 8 must be greater than 0,
    but taking the index of 0 as left end will produce a bigger ramp.

    """
    print(array)
    # produce stack
    stack=[0]
    for i in range(1,len(array)):
        print('i=',i,'compare',array[i],array[stack[-1]])
        if array[i] < array[stack[-1]]:
            stack.append(i)
            print('stack',stack)
    print(stack)
    result=0
    for i in range(len(array)-1,-1,-1):
        print('outside loop',i)
        while len(stack)!=0 and array[stack[-1]] < array[i]:
            print('loop','i',i,'stack',stack)
            result = max(result,i-stack.pop())
    return result

if __name__ == '__main__':
    l = [6,0,8,2,1,5]
    print(maxWidthRamp_2ptr(l))
    print('-------------------------')
    k=[9,8,1,0,1,9,4,0,4,1]
    print(maxWidthRamp_2ptr(k))
    print('-------------------------')
    print(maxWidthRamp_stack(k))
    print('-------------------------')
    print(maxWidthRamp_stack(l))
