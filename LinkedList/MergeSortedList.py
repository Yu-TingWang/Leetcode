from leetcode.LinkedList import ListNode

"""
LeetCode No.23
https://leetcode.com/problems/merge-k-sorted-lists/
Given a list of sorted LinkedList, merge them into a sorted LinkedList and return it
There is another solution using heap
"""

def mergeLists(lists)->ListNode:
    """ A divide and conquer solution with helper method
    """
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l = mergeLists(lists[:mid])
    r = mergeLists(lists[mid:])
    return merge(l, r)

def merge(l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next
import heapq
def mergeKLists(lists:list)->ListNode:
    '''
    lists: list of ListNodes
    '''
    heap =[]
    heapq.heapify(heap)
    for i in range(len(lists)):
        curr = lists[i]
        while curr:
            heapq.heappush(heap,curr.val)
            curr = curr.next
    dummy = ListNode()
    curr = dummy
    while heap:
        curr.next = ListNode(heapq.heappop(heap))
        curr = curr.next
    return dummy.next

from heapq import heapify,heappop,heappush,heapreplace
def mergeK_linkedList(lists:list)->ListNode:
    heap = [[head.val,i,head] for i,head in enumerate(lists) if head]
    heapify(heap)
    dummy = ListNode()
    curr = dummy
    while heap:
        val,i,node = heap[0]
        if not node.next:
            heappop(heap)
        else:
            heapreplace(heap,[node.next.val,i,node.next])
        curr.next = node
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    pass