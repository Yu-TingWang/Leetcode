import collections

from leetcode.BinaryTree import Node

def dfs_paths(root:Node) -> list:
    """ dfs + recursion
    Return a list of paths from root to children
    """
    if not root:
        return []
    result = []
    dfs(root, [], result)
    return result

def dfs(root:Node,curr_path:list,result:list)->None:
    """
    :param root: the root node of the tree
    :param curr_path:
    :param result:
    :return: nothing
    """
    if not root.left and not root.right: # a child
        result.append(curr_path+[root.val])
    if root.left:
        dfs(root.left,curr_path+[root.val],result)
    if root.right:
        dfs(root.right,curr_path+[root.val],result)

def bfs_path(root:Node)->list:
    """ bfs + queue
    Return a list of paths from root to all children
    """
    if not root: return []
    result=[]
    queue= [(root,[])]
    while queue:
        node , path = queue.pop(0)
        print(node.val,path)
        if not node.left and not node.right: # children
            result.append(path+[node.val])
        if node.left:
            queue.append((node.left,path+[node.val]))
        if node.right:
            queue.append((node.right,path+[node.val]))
    return result

def sumNumbers(root:Node) -> int:
    """
    Return the sum of the tree such that each path from root to children is a number
        1
       / \   :    will be 12+13 = 25.
      2  3
    """
    return sumNode(root,0)

def sumNode(root,curr):
    if not root:
        return 0
    if not root.left and not root.right: # children
        return curr*10 + root.val
    return sumNode(root.left,curr*10+root.val) + sumNode(root.right,curr*10+root.val)


def convert(data):
    """Converts data from string to list
    """
    n = len(data)
    data = data[1:n - 1]  # remove '[' ']'
    array = data.split(',')
    for i in range(len(array)):
        array[i]=convert(array[i])
    return array


if __name__=='__main__':
    l = [[1,2],[2,None],[None,4,5]]
    array = str(l)
    tree = convert(array)
    print(tree)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left =Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    paths = bfs_path(root)

    dfs_paths = dfs_paths(root)
    #print("output of bfs_path",paths)
    #print(dfs_paths)
