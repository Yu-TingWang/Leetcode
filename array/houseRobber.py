'''
https://leetcode.com/problems/house-robber/description/
No.198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.
---------------------------
https://leetcode.com/problems/house-robber-ii/
No.213. House Robber II
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
---------------------------
https://leetcode.com/problems/house-robber-iii/
No.337. House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
'''

def rob(nums:list)->int:
    '''
    states[i] is the maximum sum we can rub if we run i-th house as last house.
    '''
    if len(nums)==0:return 0
    if len(nums)<3: return max(nums)
    states = [0]*len(nums)
    states[0] = nums[0]
    states[1] = nums[1]
    states[2] = nums[2] + nums[0]
    for i in range(3,len(states)):
        states[i] = max(states[i-2],states[i-3])+nums[i]
    return max(nums[-1],nums[-2])

def robber(nums:list)->int:
    rob , not_rob = 0,0
    for num in nums:
        rob ,not_rob = not_rob + num, max(rob,not_rob)
    return max(rob,not_rob)

def robber2(nums:list)->int:
    if not nums: return 0
    elif len(nums)==1: return nums[0]
    else:
        return max(robber(nums[1:]),robber(nums[:-1]))

def rob2(nums:list)->int:
    '''
    since we cannot select head and tail together,
    we seperate them into two lists, when with every but head, when with everything but tail
    and compare the value of the two
    '''
    if len(nums)==0:return 0
    if len(nums)==1:return nums[0]
    numshead = nums[:len(nums)-1]
    numstail = nums[1:]
    return max(rob(numshead),rob(numstail))

from leetcode.BinaryTree import Node
def rob3(root:Node)->int:
    return max(help3(root))

def help3(root:Node):
    '''
    return a tuple (val1,val2)
    where val1 is the max amount when rob this node
          val2 is the max amount when not rob this node
    '''
    if root==None: return (0,0) # leaf node
    rob_left, xrob_left = help3(root.left) # max amount to rob and not to robe its left node
    rob_right, xrob_right = help3(root.right) # max amount to rob and not to robe its right node
    xrob_this = max(rob_left,xrob_left) + max(rob_right,xrob_right) # max amount not to rob at this node
    rob_this = xrob_left + xrob_right + root.val
    return (rob_this,xrob_this)


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(3)
    #root.left.left = Node()
    root.left.right = Node(3)
    #root.right.left = Node(6)
    root.right.right = Node(1)
    print(root)
    print(rob3(root))