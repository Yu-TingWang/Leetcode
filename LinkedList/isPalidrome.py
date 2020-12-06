from leetcode.LinkedList import ListNode
'''
https://leetcode.com/problems/palindrome-linked-list/
No.234 Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
do it in O(n) time and O(1) space
'''
def isPalindrome(head:ListNode)->bool:
    """
    first, we use fast and slow pointer to get the middle node
    --> this should take O(n/2) time and take O(2) space for pointers
    second, we reverse the second half of the list
    --> this should take o(n/2) time since we call recursion for n/2 time
    finally, we compare the first half list ane the reverse second half list,
    --> this should take O(n/2) time and no extra space is taken.
    Hence we achieve O(n) time and O(1) space.
    """
    # get the middle node
    slow = fast = head
    while fast!=None and fast.next!=None: # this should take O(n/2) time
        slow = slow.next
        fast = fast.next.next
    # reverse the second half list
    def reverse(head,prev=None):
        if head==None: return prev
        curr = head.next
        head.next = prev
        return reverse(curr,head)
    second_head = reverse(slow) # take O(n/2) time
    # compare the first half with the reverse second half
    head1 = head
    head2 = second_head
    while head1!=slow: # take O(n/2) time
        if head1.val!=head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True