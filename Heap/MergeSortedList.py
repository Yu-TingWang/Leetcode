from LinkedList import ListNode

"""
LeetCode No.23
https://leetcode.com/problems/merge-k-sorted-lists/
Given a list of sorted LinkedList, merge them into a sorted LinkedList and return it
"""

def mergeKLists(lists) -> ListNode:
    """
    Use a minheap. insert every node to the heap, and extract from the heap to construct the new LinkedList
    when finished extracting, insert the next node of the extracted node
    """
    dummy = ListNode()
    curr = dummy
    import heapq
    # from queue import PriorityQueue
    heap = heapq()
    # put the linkedlists into the heap
    for node in lists:
        if node:
            heap.put((node.val,node))
    while heap:
        # extract from the heap
        curr.next = heap.get()[1]
        # update the cursor
        curr = curr.next
        if curr.next:
            # put the next node of this linkedlist into heap
            heap.put((curr.next.val,curr.next))
    return dummy.next