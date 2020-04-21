from LinkedList import ListNode

"""
Given a list of sorted LinkedList, merge them into a sorted LinkedList and return it
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

def mergeKLists(lists) -> ListNode:
    if lists == None or lists==[]: return None
    else:
        # construct the queue first
        queue=[]
        # build the lists based on the queue
        dummy = tail = ListNode()

        while queue!=[]:
            tail.next = queue.pop(0)
            tail = tail.next
            if tail.next!=None:
                queue.append(queue.tail.next)

        return dummy.next


