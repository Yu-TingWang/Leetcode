from leetcode.BinaryTree import Node
"""
Given a list of integer, construct a height balanced binary search tree (AVL tree)
"""

def listToBST(array:list)->Node:
    array.sort()
    return construct(array)

def construct(array:list)-> Node:
    if array==[]:
        return None
    mid = len(array)//2
    root = Node(array[mid])
    root.left = construct(array[:mid])
    root.right = construct(array[mid+1:])
    return root