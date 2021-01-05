from leetcode.LinkedList import ListNode, linkedList_builder
'''
No.83 Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
--------------------------------------------
No.82 Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''
def removeI(head:ListNode)->ListNode:
    '''
    delete all duplicates such that each element appears only once
    '''
    dummy = ListNode()
    dummy.next = head
    prev = dummy  # points to the last node of the distinct linkedlist
    curr = head
    while curr:
        # points to the last node of duplicated value
        while curr and curr.next and curr.val==curr.next.val:
            curr = curr.next
        prev.next = curr
        prev = prev.next
        curr = curr.next
    return dummy.next

def removeII(head:ListNode)->ListNode:
    '''
    delete all nodes that have duplicate numbers
    '''
    from collections import defaultdict
    d = defaultdict(lambda:0)
    curr = head
    while curr:
        d[curr.val]+=1
        curr = curr.next
    dummy = ListNode()
    dummy.next = head
    curr = dummy
    # curr points to the last node that is non-duplicated
    # curr.next is kept being updated
    while curr.next:
        if d[curr.next.val] !=1:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


if __name__ == '__main__':
    head = linkedList_builder([1,1,2,2,3,4,5])
    #print(removeI(head))
    print(removeII(head))