from leetcode.BinaryTree import Node


def resursiveBuild(inorder:list,postorder:list)->Node:
    n = len(inorder)
    d={}
    for i,num in enumerate(inorder):
        d[num] = i
    return build(inorder,postorder,0,n-1,d)


def build(inorder,postorder,startin,endin,d):
    '''Helper method for recursiveBuild
    inorder:list , in each call, we only need inorder[startin:endin]
    preorder :list
    startin: the start index of inorder that we need to traverse
    endin: the end index of inorder that we need to traverse
    postindex: the index of root in postorder.
    d: map from value to its index in inorder
    '''
    if not postorder or startin> endin: return None
    root = Node(postorder.pop())
    root_index = d[root.val] # find the index of root value in inorder
    # we can't reverse the order of building right and left tree i.e. can't swap line 25 &26
    root.right = build(inorder,postorder,root_index+1,endin,d)
    root.left = build(inorder,postorder,startin,root_index-1,d)
    return root

def buildTree(inorder: list, postorder: list) -> Node:
    """Construct a binary tree from inorder and postorder """
    if len(inorder)==0:return None
    if len(inorder)==1: return Node(inorder.pop())
    root_index = backward_traverse(inorder,postorder)
    root = Node(postorder[root_index])
    root_index = inorder.index(root.val)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    root.left = buildTree(left_inorder,postorder)
    root.right = buildTree(right_inorder,postorder)
    return root


def backward_traverse(inorder,postorder)->int:
    ''' A helper method for buildTree
    traverse from the back of postorder, return the first index when its element is in inorder
    '''
    in_set = set(inorder)
    for i in range(len(postorder)-1,-1,-1):
        if postorder[i] in in_set:
            return i

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    post = [9,15,7,20,3]
    tree = buildTree(inorder,post)
    print(tree)
    tr = resursiveBuild(inorder,post)
    print(tr)
