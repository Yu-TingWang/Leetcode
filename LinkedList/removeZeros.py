from leetcode.LinkedList import ListNode as Node, ListNode

"""
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
LeetCode No.1171
"""
def removeZeroSumSublists(head: Node) -> Node:
    """Repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
    """
    prefix=0
    dummy=Node(0)
    dummy.next = head
    # construct a dictionary that maps cumulative sum to the current node
    seen ={prefix:dummy}
    curr = dummy
    while curr:
        prefix += curr.val
        seen[prefix]=curr
        curr = curr.next
    # if two nodes had the same prefix, then the nodes between them must has zero sums
    prefix=0
    curr = dummy
    while curr!=None:
        prefix += curr.val
        curr.next = seen[prefix].next
        curr = curr.next
    return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-3)
    print(head)
    print(removeZeroSumSublists(head))
    h = ListNode()


