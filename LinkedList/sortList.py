from LinkedList import ListNode
import heapq

def sortList(head: ListNode) -> ListNode:
    array=[]
    curr = head
    while curr:
        array.append(curr.val)
        curr=curr.next
    heapq.heapify(array)
    curr = head
    while curr:
        curr.val = heapq.heappop(array)
        curr=curr.next
    return head