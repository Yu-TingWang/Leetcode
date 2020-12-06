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

