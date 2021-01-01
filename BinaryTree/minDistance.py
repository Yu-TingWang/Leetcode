from leetcode.BinaryTree import Node
'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
LeetCode No.236
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as 
descendants (where we allow a node to be a descendant of itself).”
'''

def leastCommonAncestor(root:Node,p:Node,q:Node)->Node:
    stack = [root]
    # for all nodes above p or q, create a mapping from the node to its parent
    parents = {root:None}
    while p not in parents or q not in parents:
        curr = stack.pop()
        if curr.right:
            parents[curr.right] = curr
            stack.append(curr.right)
        if curr.left:
            parents[curr.left] = curr
            stack.append(curr.left)
    # get all p's ancestors
    ancestors = set()
    while p:
        p = parents[p]
        ancestors(p)
    # if in first iteration, q is in ancestors, then q is p's ancestor, which means q is the lca of q & p
    # otherwise, keep getting q's parent
    while q not in ancestors:
        q = parents[q]
    return q

def lca(root:Node, p:Node, q:Node) -> Node:
    """Return the lowest common ancestor of p and q"""
    if root is None or root== p or root== q: return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left != None and right != None: return root
    else: return left if left else right

# Returns true if there is a path from  root to the given node. It also populates 'arr' with the given path
def findPath(root:Node, arr:list, x:int):
    # if root is None there is no path
    if (not root): return False
    # push the node's value in 'arr'
    arr.append(root.val)
    # if it is the required node ,return true
    if (root.val == x): return True
    # else check whether the required node  lies in the left subtree or right  subtree of the current node
    if (findPath(root.left, arr, x) or findPath(root.right, arr, x)):
        #print(arr)
        return True
    # required node does not lie either in  the left or right subtree of the current  node.
    # Thus, remove current node's value from 'arr'and then return false
    arr.pop()
    return False
"""
Amazon OA:
Find distance between two nodes of a Binary Tree
Find the distance between two keys in a binary tree, no parent pointers are given. Distance between two
nodes is the minimum number of edges to be traversed to reach one node from other.
"""
def minDistance(root:Node, p:Node, q:Node) -> int:
    parent = lca(root, p, q)
    #print(parent.val)
    parent_p = []
    findPath(parent, parent_p, p.val)
    #print(parent_p)
    parent_q = []
    findPath(parent, parent_q, q.val)
    #print(parent_q)
    # minus 2 cuz root is included in the array
    return len(parent_p)+len(parent_q)-2

def distanceK(root:Node,target:Node,k:int)->list:
    """Return a list of nodes that has distance k with target node"""
    from leetcode.BinaryTree.dfs import InOrder
    nodes = InOrder(root)
    result=[]
    for i in range(len(nodes)):
        if minDistance(root,target,nodes[i])==k:
            result.append(nodes[i])
    return nodes[i]




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
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
    second = root.left
    p = root.left.right
    q = root.left.left.right
    print(minDistance(root,q,p))
    """
    parent = lca(root,p,q)
    print(parent.val)
    a=[]
    findPath(parent,a,q.val)
    print(a)
    print(minDistance(root,p,q))
    b = []
    findPath(parent,b,2)
    print(b)
    
    q_path = []
    pathToNode(root,q_path,q.val)
    print(path)
    print(q_path)
    """
