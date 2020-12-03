from leetcode.BinaryTree import Node
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
https://leetcode.com/problems/sum-root-to-leaf-numbers/
LeetCode No.129
'''

def sumPaths(root:Node)->int:
    if not root: return 0
    result = []
    queue = [(root, '')]
    while queue:
        curr = queue.pop(0)
        node = curr[0]
        path = curr[1]
        update_path = path + str(node.val)
        if not node.left and not node.right:  # children
            result.append(update_path)
        if node.left:
            queue.append((node.left, update_path))
        if node.right:
            queue.append((node.right, update_path))
    return sum([int(path) for path in result])

def sumNumbers(root:Node) -> int:
    # get the list of paths from root to all children
    paths = path(root)
    print(paths)
    total = 0
    for i in range(len(paths)):
        n = len(paths[i]) - 1
        for j in range(len(paths[i])):
            print('i',i,'j',j,'n',n,'this_path:',paths[i][j] * (10 ** (n - j)))
            total += paths[i][j] * (10 ** (n - j))
    return total

def path(root: Node) -> list:
    if not root: return []
    result = []
    queue = [(root, [])]
    i=0
    while queue:
        curr = queue.pop(0)
        node = curr[0]
        path = curr[1]
        print('i',i,'node',node.val,'path',path,'queue',queue)

        if not node.left and not node.right:  # children
            result.append(path + [node.val])
        if node.left:
            queue.append((node.left, path + [node.val]))
        if node.right:
            queue.append((node.right, path + [node.val]))
        i+=1
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
    print(path(root))
    print('--------------')
    print(sumNumbers(root))
    print('--------------')
    print(sumPaths(root))
    # r = Node(4)
    # r.left = Node(2)
    # r.left.left = Node(1)
    # r.left.right = Node(3)
    # r.right = Node(7)
    # r.right.left = Node(6)
    # r.right.right = Node(8)
    # print(path(r))