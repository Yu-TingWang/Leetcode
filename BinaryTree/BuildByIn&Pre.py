from leetcode.BinaryTree import Node

"""
Given list of inorder and preorder traversal,construct a binary tree.
"""


def recursiveBuild(inorder: list, preorder: list) -> Node:
    n = len(inorder)
    d = {}
    for i,num in enumerate(inorder):
        d[num] = i
    return build(inorder, preorder, 0, n - 1, d)

def build(inorder, preorder, startin, endin,d):
    ''' Helper method for recursiveBuild
    inorder: list , in each call, we only need inorder[startin:endin]
    preorder :list
    startin: the start index of inorder that we need to traverse
    endin: the end index of inorder that we need to traverse
    prestart: the index of our current root.
    d: map from value to its index in inorder
    '''
    if not preorder or startin> endin:
        return None
    # root = Node(preorder[prestart])
    root = Node(preorder.pop(0))
    root_index = d[root.val] # get the index in inorder such that inorder[index] == root.val
    # root.left = build(inorder,preorder,startin,root_index-1,prestart+1,d)
    root.left = build(inorder, preorder, startin, root_index - 1, d)
    # since preorder visit nodes on left before going to the right, thus we can get the immediate right child index 
    # by skipping all the node on the left subtrees of current node. 
    # the inorder array has this information about how many nodes are in left subtree and right subtree. 
    # so the immediate right child index is :
    # prestart + |Node on left-tree| + 1, where |Node on left-tree| = index(root) - startin
    # so prestart' = prestart + index - startin + 1
    # root.right = build(inorder,preorder,root_index+1,endin,prestart+root_index-startin+1,d)
    root.right = build(inorder,preorder,root_index+1,endin,d)
    return root



'''
Note:
Preorder (root,left,right)
Inorder  (left,root,right)
Approach:
So root will be preorder[0], let i = inorder.index(preorder[0]).
So inorder[:i] is left substree and inorder[i+1:] is right subtree.
To decide the value of root.left -->for num in inorder[:i], the first one we match at preorder[1:].
Once we found that number at preorder, find the index of that number in inorder, and split it again.
To decide the value of root.right --> for num in inorder[i+1:], the first one we match at preorder[1:],
once we found that number at preorder, find the index that number in inorder, and split it again.
'''


def buildTree(inorder: list, preorder: list) -> Node:
    """Construct a binary tree from inorder and preorder """
    if not inorder:
        return None
    # why use inorder not preorder? cuz the recursive call will shorten inorder but pre is the same
    if len(inorder) == 1:
        return Node(inorder.pop())
    root_index = traverse(inorder, preorder)
    root_val = preorder[root_index]
    split_index = inorder.index(root_val)
    # slice inorder to left and right
    left_in = inorder[:split_index]
    right_in = inorder[split_index + 1:]
    # print('r_i',root_index,'s_i',split_index,'left_in',left_in,'right_in',right_in)
    root = Node(root_val)
    root.left = buildTree(left_in, preorder)
    root.right = buildTree(right_in, preorder)
    return root


def traverse(inorder, preorder) -> int:
    """Helper method for buildTree
    Traverse from left of preorder, return the first index whose element is in inorder.
    """
    in_set = set(inorder)
    for i in range(len(preorder)):
        if preorder[i] in in_set:
            return i


if __name__ == "__main__":
    # preorder =[1,2,4,8,9,10,11,5,3,6,7]
    # inorder = [8,4,10,9,11,2,5,1,6,3,7]
    # tree = buildTree(inorder,preorder)
    # print(tree)
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    t = buildTree(ino, pre)
    print(t)
    te = recursiveBuild(ino,pre)
    print(te)

