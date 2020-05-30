"""
Given an array nums of n integers, a target integer, and a targeted number of element k,
Find all set of unique k numbers in the array which gives the sum of target.
Restriction: The solution set must not contain duplicate k numbers
"""

def kSum(nums:list,target:int,k:int):
    """
    Find the list of k integers that sums to target.
    :param nums: list[int], the input array of integers
    :param target: the target sum
    :param k: the number of integer sums up to target
    :return: the list containing the solution
    """
    result=[]
    ksum_helper(nums,target,k,[],result)
    return result


def ksum_helper(nums:list,target:int,k:int,lst:list,result:list):
    """
    Modify result such that result contains the solution to kSum
    Takes O(n^(k-1)) time.
    :param nums: list[int] , the input array of integers
    :param target: the target sum
    :param k: the number of integer added up to target sum
    :param lst: the inner list inside result
    :param result: the list that contains the solution
    :return: None
    """
    # print("target:",target,";k:",k,";lst:",lst)
    if not nums or len(nums)<k or k<2:
        return
    nums.sort() # O(nlogn)
    if k==2: # base case
        start,end = 0,len(nums)-1
        while start<end :
            sums = nums[start]+ nums[end]
            if sums==target:
                result.append(lst+[nums[start],nums[end]])
                start+=1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
            elif sums<target:
                start+=1
            else:
                end-=1
    else: # call recursion
        for i in range(len(nums)-k+1):
            if i==0 or (i>0 and nums[i-1]!=nums[i]):
               ksum_helper(nums[i+1:],target-nums[i],k-1,lst+[nums[i]],result)

if __name__ == '__main__':
    array =[1,0,-1,0,-2,2]
    input=[-1,0,1,2,-1,-4]
    #sort =[-2,-1,0,0,1,2]
    result = []
    #ksum_helper(array,0,4,[],result)
    
    print(kSum(input,0,3))
    #print(result)