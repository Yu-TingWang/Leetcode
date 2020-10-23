from BinaryTree import Node

"""
**** This is buggy
def resursiveBuild(inorder:list,postorder:list)->BinaryNode:
    n = len(inorder)
    d={}
    for i in range(n):
        d[inorder[i]]=i

    def build(inorder,postorder,startin,endin,postindex,d):
        if startin>endin:
            return None
        curr = postorder[postindex[0]]
        node = BinaryNode(curr)
        postindex[0]-=1
        if startin==endin:
            return node
        index=d[curr]
        node.right = build(inorder,postorder,index+1,endin,postindex,d)
        node.left = build(inorder,postindex,startin,index-1,postindex,d)
        return node

    return build(inorder,postorder,0,n-1,[n-1],d)
"""


def buildTree(inorder: list, postorder: list) -> Node:
    """Construct a binary tree from inorder and postorder """
    if inorder == []:
        return None
    if len(inorder) == 1:
        return Node(inorder.pop())

    def traverse(inorder, postorder) -> int:
        """Traverse from right of postorder, return the first index
        whose element is in inorder.
        """
        in_set = set(inorder)
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] in in_set:
                return i

    root_index = traverse(inorder, postorder)
    root_val = postorder[root_index]

    def search(inorder, val) -> int:
        """Return the index where its element is val"""
        for i in range(len(inorder)):
            if inorder[i] == val:
                return i

    split_index = search(inorder, root_val)
    # slice inorder to left and right
    left_in = inorder[:split_index]
    right_in = inorder[split_index + 1:]
    root = Node(root_val)
    root.left = buildTree(left_in, postorder)
    root.right = buildTree(right_in, postorder)
    return root
