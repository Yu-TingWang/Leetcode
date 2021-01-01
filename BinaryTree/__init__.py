class Node():
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

    def __str__(self):
        root = self
        result = []
        if root == None:
            return result
        queue = []
        queue.append(root)
        while queue != []:
            size = len(queue)
            curr_level = []
            for i in range(size):
                curr = queue.pop(0)
                if curr!=None:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    curr_level.append(curr.val)
                else:
                    curr_level.append(None)
            result.append(curr_level)
        result.pop()# remove the last list which is all null
        return str(result)

def buildTree(values:list):
    '''
    Built a BST given a list of values
    '''
    root = None
    for val in values:
        root = insert(root,val)
    return root

def buildBalanceTree(values:list):
    '''
    Built a height-balance tree given a list of values
    '''
    levels = split_level(values)


def split_level(values:list):
    '''
    Built a height-balance tree given a list of values
    '''
    # split the list to level order
    result = []
    import math
    level = math.log(len(values),2)
    i=0
    while i<level:
        curr_level = []
        for j in range(2**i):
            if len(values)==0:
                break
            else:
                curr_level.append(values.pop(0))
        result.append(curr_level)
        i+=1
    return result

def insertBalance(root:Node,val):
    if root==None:
        return Node(val)
    if root.left==None:
        root.left = Node(val)
    elif root.right==None:
        root.right = Node(val)
    return root


def insert(root:Node,val):
    '''
    insert a node with given value into the tree, and return the root
    '''
    if root==None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root

def delete(root:Node,val):
    '''
    delete a node with given val in a BST, and return the root.
    recursive approach
    '''
    if not root: return
    if val>root.val:
        root.right = delete(root.right,val)
    elif val < root.val:
        root.left = delete(root.left,val)
    else:
        if root.val!=val:return root
        # if root is to be deleted
        # case 1: the subtree does not have a left child, return its right child to its parent
        if not root.left:
            return root.right
        # case 2: the subtree does have a left child, find its max child and replace it with its val.
        # why max child ? because the root value
        else:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            # replace
            root.val = tmp.val
            root.left = delete(root.left,tmp.val)
    return root

    # parent = None # ptr to parent node of current node
    # curr = root
    # # find the node and its parent to delete
    # while curr and curr.val!=val:
    #     parent = curr
    #     if parent.val < val:
    #         curr = curr.right
    #     else:
    #         curr = curr.left
    # # the node to be deleted has no children
    # if not curr.left and not curr.right:
    #     if curr==root:# it means that the tree only has root node
    #         root= None
    #     else:
    #         if parent.left == curr:
    #             parent.left = None
    #         else:
    #             parent.right = None
    # # the node to be deleted has two children
    # elif curr.left and curr.right:
    #     # find the sucessor and its parent
    #     parent_successor , suc = successor(curr)
    #     curr.val = suc.val
    #     if parent_successor.left == suc:
    #         parent_successor.left = None
    #     else:
    #         parent_successor.right = None
    # # the node to be deleted has one children
    # else:
    #     if not curr.left: # curr has right child
    #         if parent.left==curr:
    #             parent.left = curr.right
    #         else:
    #             parent.right = curr.right
    #     else: # curr has left child
    #         if parent.left==curr:
    #             parent.left = curr.left
    #         else:
    #             parent.right = curr.left

def iterative_helper(root:Node):
    '''
    helper function for delete_iterative.
    Remove a bst rooted at root, remove the root, do the necessary adjustment and return the new root
    '''
    if root == None:
        return root
    # if this node has fewer than 2 child, return the non-null child.
    if root.left == None:
        return root.right
    if root.right == None:
        return root.left
    # if the node has two children, get the min child and its parent in our right sub-tree
    curr, parent = root.right, None
    while curr.left!=None:
        # print('curr',curr,'parent',parent)
        parent, curr = curr, curr.left
    # print('curr', curr, 'parent', parent)
    # print('curr.left',curr.left,'root.left',root.left)
    # curr is going to be our new root, transplant the original left subtree to be the left subtree of our new root
    curr.left = root.left
    # if curr == root.right, then there is only one node in the right subtree, take this as new root and return it
    # else transplant the original right subtree to be the right subtree of our new root
    if root.right!=curr:
        print('parent.left',parent.left,'curr.right',curr.right)
        parent.left = curr.right # remove curr from the old right subtree
        print('curr.right', curr.right, 'root.right', root.right)
        curr.right = root.right # transplant the old right subtree under the new root
    return curr

def delete_iterative(root:Node,val):
    curr,parent = root, None
    # get the node to delete and its parent
    while curr!=None and curr.val !=val:
        parent = curr
        if val<curr.val:
            curr = curr.left
        elif val >curr.val:
            curr = curr.right
    # print(curr)
    if not curr or curr.val!=val: return root
    # if parent is null, that means root is the node to be deleted
    if not parent:
        return iterative_helper(curr)
    if parent.left == curr:
        parent.left = iterative_helper(parent.left)
    else:
        parent.right = iterative_helper(parent.right)
    return root




if __name__ == '__main__':
    # val  = [4,5,6,1,2,3]
    # expected = [[4],[5,6],[1,2,3]]
    # print(buildBalanceTree(val))
    # print('expected',expected)
    # r = buildTree(val)
    # print(r)
    root = Node(8)
    root.left = Node(4)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.left.left.right = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    root.right = Node(12)
    root.right.left = Node(10)
    root.right.left.left = Node(9)
    root.right.left.right = Node(11)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.right.right.right = Node(15)
    print(root)
    print('=====')
    root = iterative_helper(root)
    print('+++++++')
    print(root)
    print('+++++++')
    '''
              4
           /     \
          2       6
        /  \     /  \
      1     3   5    7
    '''
    # # delete(root,3)
    # # print(root)
    # # root = insert(root,8)
    # # print(root)
    # root = delete_iterative(root,8)
    # print(root)
    # root = delete_iterative(root, 4)
    # print(root)
    # root = delete_iterative(root, 4)
    # print(root)
    # print('-----')
    # # delete(root,4)
    # # print(root)
    # r = Node(4)
    # r.left = Node(2)
    # r.right = Node(6)
    # r.left.left = Node(1)
    # r.left.right = Node(3)
    # r.right.left = Node(5)
    # r.right.right = Node(7)
    # print(r)
    # r = delete(r,0)
    # print(r)
    # # r = delete(r,3)
    # # print(r)
    # # r = delete(r,6)
    # # print(r)
