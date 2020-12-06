from leetcode.LinkedList import ListNode
'''
https://leetcode.com/problems/partition-list/
No.86 Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''
def partition(head:ListNode,x:int)->ListNode:
    # seperate the list into 2 lists, one with elements smaller than x, one otherwise
    small_dummy = s_curr = ListNode()
    bigger_dummy = b_curr = ListNode()
    curr = head
    while curr!=None:
        if curr.val<x:
            s_curr.next = ListNode(curr.val)
            s_curr = s_curr.next
        else:
            b_curr.next = ListNode(curr.val)
            b_curr = b_curr.next
        curr = curr.next
    s_curr.next = bigger_dummy.next
    return small_dummy.next

