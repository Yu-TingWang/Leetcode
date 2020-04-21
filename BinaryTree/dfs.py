class Node():
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None
"""
Given the root, return a list of nodes in the tree
"""


def InOrder(root)->list:
    ''' left -> root -> right '''
    if root==None:
        return []
    stack=[]
    curr=root
    result=[]
    while True:
        if curr!=None:
            stack.append(curr.left)
            curr=curr.left
        elif stack!=[]:
            curr = stack.pop()
            result.append(curr.val)
            curr =curr.right
        else:
            break
    return result

def PostOrder(root)->list:
    ''' left -> right -> root '''
    if root==None:
        return []
    roots=[]
    roots.append(root)
    stack=[]
    while roots!=[]:
        curr = roots.pop()
        stack.append(curr)
        if curr.left!=None:
            roots.append(curr.left)
        if curr.right!=None:
            roots.append(curr.right)
    result =[]
    for i in range(len(stack)):
        result.append(stack[i].val)
    return result[::-1]

def PreOrder(root:Node) ->list:
    ''' root -> left -> right '''
    if root==None:
        return []
    stack=[]
    stack.append(root)
    result=[]
    while stack!=[]:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right!=None:
            stack.append(curr.right)
        if curr.left!=None:
            stack.append(curr.left)
    return result

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
