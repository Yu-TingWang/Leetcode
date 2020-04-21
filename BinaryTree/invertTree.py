from BinaryTree import Node
"""
Invert a Binary Tree
ex.      1                      1
      /    \                  /   \
    2       3              3       2 
  /  \     /  \           / \     /  \
4     5   6    7         7   6   5    4
"""
def invert_recursive(root:Node):
    if not root:
        return None
    left = invert_recursive(root.right)
    root.right = invert_recursive(root.left)
    root.left = left
    return root

def invert_stack(root:Node):
    if not root:
        return None
    stack=[root]
    while stack:
        curr = stack.pop()
        left = curr.left
        curr.left = curr.right
        curr.right = left
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return root

def invert_bfs(root:Node):
    if not root:
        return None
    queue=[root]
    while queue:
        curr = queue.pop(0)
        left = curr.left
        curr.left = curr.right
        curr.right = left
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return root