from leetcode.BinaryTree import Node

'''
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
No.1315 Sum of Nodes with Even-Valued Grandparent
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.
'''


def sumEvenGrandparent(root: Node) -> int:
    # for parent_val and grandparent_val , just put whatever odd number since the root do not have parent/grandparent yet
    return helper(root, 1, 1)


def helper(curr: Node, parent_val: int, grandparent_val: int):
    return helper(curr.left, curr.val, parent_val) + \
           helper(curr.right, curr.val,parent_val) + \
           curr.val if not curr and grandparent_val % 2 == 0 else 0
    # if not curr: return 0
    # if curr:
    #     if grandparent_val&2==0:
    #         return curr.val + helper(curr.left,curr.val,parent_val)+helper(curr.right,curr.val,parent_val)+ curr.val
    #     else:
    #         return helper(curr.left,curr.val,parent_val)+helper(curr.right,curr.val,parent_val)
