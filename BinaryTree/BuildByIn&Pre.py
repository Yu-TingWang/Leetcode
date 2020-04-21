from BinaryTree import Node
def recursiveBuild(inorder: list, preorder: list) -> Node:
    n = len(inorder)
    d = {}
    for i in range(n):
        d[inorder[i]] = i

    def build(inorder, preorder, startin, endin, preindex, d):
        if startin > endin:
            return None
        curr = preorder[preindex[0]]
        node = Node(curr)
        preindex[0] += 1
        if startin == endin:
            return node
        index = d[curr]
        node.right = build(inorder, preorder, index + 1, endin, preindex, d)
        node.left = build(inorder, preindex, startin, index - 1, preindex, d)
        return node

    return build(inorder, preorder, 0, n - 1, [0], d)


def buildTree(inorder: list, preorder: list) -> Node:
    """Construct a binary tree from inorder and preorder """
    if inorder == []:
        return None
    if len(inorder) == 1:
        return Node(inorder.pop())

    def traverse(inorder, preorder) -> int:
        """Traverse from right of preorder, return the first index
        whose element is in inorder.
        """
        in_set = set(inorder)
        for i in range(len(preorder)):
            if preorder[i] in in_set:
                return i

    root_index = traverse(inorder, preorder)
    root_val = preorder[root_index]

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
    root.left = buildTree(left_in, preorder)
    root.right = buildTree(right_in, preorder)
    return root

