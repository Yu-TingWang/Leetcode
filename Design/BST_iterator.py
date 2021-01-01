'''
https://leetcode.com/problems/binary-search-tree-iterator/
No.173 Binary Search Tree Iterator
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of
the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height(tree)?
'''
from leetcode.BinaryTree import Node

"""
Use a pointer that point to the current node, and a stack to store the current node's ancestor.
Since the amount of the ancestor has is equal to the height, hence the memory usage is going to be O(h).

"""


class BSTIterator:

    def __init__(self, root: Node):
        self.stack = []
        self.curr_ptr = root

    def next(self) -> int:
        node = self.curr_ptr
        while node != None:
            self.stack.append(node)
            node = node.left
        curr = self.stack.pop()
        self.curr_ptr = curr.right
        return curr.val

    def hasNext(self) -> bool:
        return self.curr_ptr is not None or self.stack != []


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    obj = BSTIterator(root)
    while obj.hasNext():
        result = obj.next()
        print(result)
    from collections import defaultdict
    j = defaultdict(lambda:1)
    j['hello'] = 'world'
    j['hi'] = 'earth'
    for key,v in j.items():
        print(key,v)