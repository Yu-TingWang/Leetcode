import BinaryTree

from BinaryTree import Node as TreeNode
from LinkedList import ListNode


def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
    return helper(head, head, root)


def helper(self, head, curr, root) -> bool:
    if curr == None:
        return True
    if root == None and curr != None:
        return False
    if root.val != curr.val:  # adjust the list or tree
        if curr != head:  # if we haven't compare the head of the list
            return helper(head, head, root)
        else:
            return helper(head, head, root.left) or self.helper(head, head, root.right)
    if root.val == curr.val:
        return helper(head, curr.next, root.left) or self.helper(head, curr.next, root.right)