'''
https://leetcode.com/problems/next-greater-element-ii/
Leetcode No.503 Next Greater Element II
Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
'''
def nextGreaterElements(nums:list)->list:
    '''
    Step 1. go through the list as if its not circular, assign the next greater number to output array
    Step 2. while step1, get the first occurrence of maximum element and its index.
    Step 3. for elements after the max element, record those who hasn't been assigned with next greater number
    Step 4. traverse nums list from the beginning, assign the first greater element to indices acquired in step 3
    Step 5. convert '#' to -1
    '''
    if len(nums)==0: return[]
    # why not just use -1 ? cuz it's possible the the actual 'next greater element' is -1
    result = ['#']*len(nums)
    max_value, max_index = nums[0] , 0
    # 1. go through the list as if its not circular
    stack = []
    for i in range(len(nums)):
        # 2. get the first occurrence of max val and its index
        if nums[i]>max_value:
            max_value = nums[i]
            max_index = i
        while stack and nums[stack[-1]] < nums[i]:
            change = stack.pop()
            result[change] = nums[i]
        stack.append(i)
    # 3. record whose hasn't been assigned value for whoever after max_index
    stack = []
    for j in range(max_index+1,len(result)):
        if result[j]=='#':
            stack.append(j)
    # 4. deal with what we collected in the stack
    i = 0
    while stack!=[] and i<=max_index:
        while stack and nums[stack[-1]]<nums[i]:
            change = stack.pop()
            result[change]=nums[i]
        i+=1
    # 5. convert '#' to -1
    for i in range(len(result)):
        if result[i] == '#':
            result[i]=-1
    return result


def loop_twice(nums:list)->list:
    '''
    In the first loop, whatever remains in the stack are those who hasn't been assign the next greater value,
    so if we keep this stack and loop the input list from the start again, we can find the next greater value.
    '''
    stack, res = [], [-1] * len(nums)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    print(res,stack)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res

if __name__ == '__main__':
    array = [1,2,3,2,1]
    #print(nextGreaterElements(array))
    print(loop_twice(array))