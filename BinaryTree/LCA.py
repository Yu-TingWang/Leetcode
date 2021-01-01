from leetcode.BinaryTree import Node

from leetcode.BinaryTree.bfs import levelOrder

def LowestCommonAncestor(root,p,q):
    """
    Recursive Approach
    """
    if root==None or p==root or q==root:
        # find p/q , return None if not found
        return root
    left = LowestCommonAncestor(root.left,p,q)
    right = LowestCommonAncestor(root.right,p,q)
    # if neither is None, then one is at left and another is at right
    # which means root must be LCA
    if left!=None and right!=None:
        return root
    else: # if left is None, then both nodes at are right sub-tree, which means
        # the LCA must be found in the right-subtree
        return left if left else right

def lca(root,p,q):
    """
    Iterative Approach
    """
    stack = [root]
    parent = {root:None} # maps from child to its parent
    # construct a map that map from all nodes from p to root, and from q to root
    while p not in parent or q not in parent:
        node = stack.pop()
        print(node.val)
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    for node in parent:
        if parent[node]:
            print(node.val,'->',parent[node].val,end=';')
        else:
            print(node.val, '->', None, end=';')
    #print([n.val]for n in stack)
    print('\n')
    ancestor = set()
    while p:
        ancestor.add(p)
        p = parent[p]
    while q not in ancestor:
        q = parent[q]
    return q

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left =Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    p = root.left.right
    q = root.left.left.right
    levels = levelOrder(root)

    for i in range(len(levels)):
        if i==0:
            print(" " * 10, end =" ")
        if i==1:
            print(" " * 8, end=" ")
        if i==2:
            print(" "*4,end=" ")
        print(levels[i])

    print("p",p.val,';q',q.val)
    print('-------------------------\n')
    #lca = LowestCommonAncestor(root,p,q)
    l = lca(root,p,q)
    print(l)

