from leetcode.LinkedList import ListNode

def reverseList(head:ListNode):
    prev=None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

def reverse_recur(head:ListNode):
    """ Reverse the List by recursion"""
    def reverse(head:ListNode,prev:ListNode):
        if not head:
            return prev
        curr = head.next
        head.next = prev
        return reverse(curr,head)
    return reverse(head,None)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(head)

    recur = reverse_recur(head)
    print(recur)