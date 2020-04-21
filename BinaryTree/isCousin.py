from BinaryTree import Node

def isCousins(root: Node, x: int, y: int) -> bool:
    """ Check if two nodes are cousins, not sibilings"""
    # find the depth and parents of both nodes
    # compare if depths are the same but parents are different
    xdepth , xparent = depth_parent(root,None,0,x)
    ydepth , yparent = depth_parent(root,None,0,y)
    return xdepth==ydepth and xparent!=yparent

def depth_parent(curr:Node,parent:Node,depth:int,target:int) :
    if curr:
        if curr.val==target:
            return parent , depth
        else:
            return (curr.left,curr,depth+1,target) or (curr.right,curr,depth+1,target)
