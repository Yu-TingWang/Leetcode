class Node():
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

def iterative_bfs(root:Node) -> list:
    """Return a list of int by level"""
    if root==None:
        return []
    queue=[]
    curr=root
    queue.append(curr)
    result=[]
    while queue!=[]:
        curr = queue.pop(0)
        result.append(curr.val)
        if curr.left!=None:
            queue.append(curr.left)
        if curr.right!=None:
            queue.append(curr.right)
    return result

def levelOrderbydfs(root:Node) -> list:
    """ Get the level order by dfs and recursion"""
    d={}
    dfs_level(root,0,d)
    if d=={}:
        return []
    else:
        n = max(d.keys())
        return [d[i] for i in range(n)]

def dfs_level(root:Node,level:int,d:dict):
    """ This is a helper function of levelOrderbydfs.
    It helps construct a dictionary that maps level to nodes in that level.
    Traverse each level by dfs.
    """
    if root!=None:
        if level not in d:
            d[level]=[]
        d[level].append(root)
        dfs_level(root.left,level+1,d)
        dfs_level(root.right,level+1,d)

def levelOrder(root:Node)-> list:
    """Return a nested list which its inner list by level.
    This is an iterative approach without helper function
    """
    result=[]
    if root==None:
        return result
    queue=[]
    queue.append(root)
    while queue!=[]:
        size = len(queue)
        curr_level = []
        for i in range(size):
            curr = queue.pop(0)
            if curr.left!=None:
                queue.append(curr.left)
            if curr.right!=None:
                queue.append(curr.right)
            curr_level.append(curr.val)
        result.append(curr_level)
    return result


if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left =Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    levels= levelOrder(root)
    iterative = iterative_bfs(root)
    print(levels)
    print(iterative)