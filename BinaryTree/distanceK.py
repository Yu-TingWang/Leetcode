import collections

from pip._vendor.msgpack.fallback import xrange

from BinaryTree import Node
from BinaryTree.minDistance import findPath, minDistance,lca
from BinaryTree.dfs import InOrder
def distanceK(root:Node,target:Node,k:int) -> list:
    """
    Return a list of the values of all nodes that have a distance K from the target node.
    :param root:
    :param target: BinaryNode
    :param k:
    :return:
    """
    # find the parent of target node
    # find the pointer of the parent of the target node?
    nodes = InOrder(root)
    result=[]
    for i in range(len(nodes)):
        if minDistance(root,target,nodes[i])==k:
            result.append(nodes)
    return result






def distance(root, target, K):
    conn = collections.defaultdict(list)

    def connect(parent, child):
        if parent and child:
            conn[parent.val].append(child.val)
            conn[child.val].append(parent.val)
        if child.left: connect(child, child.left)
        if child.right: connect(child, child.right)

    connect(None, root)
    bfs = [target.val]
    seen = set(bfs)
    for i in xrange(K):
        bfs = [y for x in bfs for y in conn[x] if y not in seen]
        seen |= set(bfs)
    return bfs