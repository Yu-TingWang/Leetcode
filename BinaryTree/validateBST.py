from BinaryTree import Node
"""
Return True if the binary Tree is a valid BST.
"""
def validate_BST(root:Node)->bool:
    from BinaryTree.dfs import InOrder
    array = InOrder(root)
    validate = array.copy()
    return array == validate.sort()

def validateBST(root:Node)->bool:
    """
    iterative solution
    using a stack to validate
    :param root:
    :return:
    """
    stack=[]
    pre = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not pre and root.val<=pre.val:
            return False
        pre = root
        root = root.right
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
