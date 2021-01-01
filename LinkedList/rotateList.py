'''
https://leetcode.com/problems/rotate-list/
Leetcode No.61 Rotate List
Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
'''
from leetcode.LinkedList import ListNode

def rotate_circle(head:ListNode,k:int)->ListNode:
    # get the length of the list
    if not head or not head.next: return head
    dummy = ListNode()
    dummy.next = head
    tail = dummy
    i=0
    # compute the length of linked list and its tail
    while tail.next:
        tail=tail.next
        i+=1
    cut_point = dummy
    # cut_point will be the new tail, cut_point.next will be the new head
    for j in range(i-k%i,0,-1):
        cut_point = cut_point.next
    # do the rotation
    tail.next = dummy.next # connect with the old tail with old head
    dummy.next = cut_point.next
    cut_point.next = None
    return dummy.next


def rotateRight_circle(head:ListNode,k:int)->ListNode:
    '''
    Approach: make it a circular linked list, and cut the connection at k point
    '''
    # get the length of the list
    if not head: return head
    tail = head
    n = 1
    while tail.next:
        tail = tail.next
        n+=1
    # connect tail with head to make it a circle
    tail.next = head
    # reduce repeated rotation
    k = k % n
    curr = head
    for i in range(n-k-1):
        curr = curr.next
    # curr is the tail we want to cut
    new_head = curr.next
    curr.next = None
    return new_head
