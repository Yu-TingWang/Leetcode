"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
LeetCode No.124
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along
the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""
from leetcode.BinaryTree import Node
from leetcode.BinaryTree.bfs import levelOrder

def maxPathSum(root:Node)->int:
    '''

    '''
    if not root: return 0
    curr_max = [root.val]
    maxPathDown(root,curr_max)
    return curr_max[0]


def maxPathDown(node:Node,curr_max)->int:
    if not node: return 0
    left = max(0,maxPathDown(node.left,curr_max))
    right = max(0,maxPathDown(node.right,curr_max))
    curr_max[0] = max(curr_max[0],left+right+node.val)
    return max(left,right) + node.val

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left =Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root.left.left.left = Node(8)
    # root.left.left.right = Node(9)
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(11)
    # root.right.left.left = Node(12)
    # root.right.left.right = Node(13)
    # root.right.right.left = Node(14)
    # root.right.right.right = Node(15)
    levels = levelOrder(root)

    for i in range(len(levels)):
        if i==0:
            print(" " * 10, end =" ")
        if i==1:
            print(" " * 8, end=" ")
        if i==2:
            print(" "*4,end=" ")
        print(levels[i])

    print('-------------------------\n')
    print(maxPathSum(root))


