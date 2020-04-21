from LinkedList import ListNode as Node

def removeZeroSumSublists(head: Node) -> Node:
    """Repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
    """
    prefix=0
    dummy=Node()
    dummy.next = head
    # construct a dictionary that maps cumulative sum to the current node
    seen ={}
    seen[prefix]=dummy
    curr = dummy
    while curr:
        prefix += curr.val
        seen[prefix]=curr
        curr = curr.next
    # if two nodes had the same prefix, then the nodes between them must has zero sums
    prefix=0
    curr = dummy
    while curr:
        prefix += curr.val
        curr.next = seen[prefix].next

    return dummy.next


