from leetcode.BinaryTree import Node
"""
Return True if the binary Tree is a valid BST.

https://leetcode.com/problems/validate-binary-search-tree/
LeetCode No.98
"""
def validate_BST(root:Node)->bool:
    from leetcode.BinaryTree.dfs import InOrder
    # inorder traversal of BST must be sorted
    array = InOrder(root)
    validate = array.copy()
    # check if its inorder is sorted
    return array == validate.sort() and len(array)==len(set(array))
class Node():
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None
def validateBST(root:Node)->bool:
    """
    iterative solution
    using a stack to validate
    :param root:
    :return:
    """
    stack=[]
    pre = None
    i=0
    while root or stack:
        print('i',i,'stack',[node.val for node in stack] )
        j=0
        while root:
            print('j',j,'stack',[node.val for node in stack] )
            stack.append(root)
            root = root.left
            j+=1
        root = stack.pop()
        if pre!=None and root.val<=pre.val:
            print('pre',pre.val,'curr',root.val)
            return False
        pre = root
        root = root.right
        i+=1
    return True


def isValidBST(root:Node, prev=None)->bool:
    """
    Using recursion to validate
    :param root:
    :param prev:
    :return:
    """
    if not root: return True
    left = isValidBST(root.left)
    if not prev and root.val<=prev.val:
        return False
    prev = root
    right = isValidBST(root.right)
    return left and right


if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left =Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    p = root.left.right
    q = root.left.left
    print(validateBST(root))
    print('--------------')
    r = Node(4)
    r.left = Node(2)
    r.left.left = Node(1)
    r.left.right = Node(3)
    r.right = Node(7)
    r.right.left = Node(6)
    r.right.right = Node(8)
    print(validateBST(r))