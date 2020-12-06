from leetcode.LinkedList import ListNode
def numComponents(self, head: ListNode, G: list) -> int:
    """Return the number of connected components in G,
     where two values are connected if they appear consecutively in the linked list.
     """
    g = set(G)
    sums = 0
    while head:
        if head.val in g and (head.next == None or head.next.val not in g):
            sums += 1
        head = head.next
    return sums