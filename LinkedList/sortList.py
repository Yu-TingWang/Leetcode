from leetcode.LinkedList import ListNode
import heapq

'''
https://leetcode.com/problems/sort-list/
No.148 Sort List
sort the linked list in ascending order with O(nlogn) time and O(1) space
There are three approachs:
sortList takes O(nlogn) time and O(1) space
recursive_sortList takes O(n logn) time and O(log n) space
sortlist takes O(n) space and O(n) space
'''


def sortList(head: ListNode) -> ListNode:
    '''
    Use merge sort (bottom-to-up), iterative approach
    '''
    if not head: return head
    n = get_length(head)  # get the length of the linked-list
    dummy = ListNode()
    dummy.next = head
    left = right = tail = None
    # step 1: divide, split each linked list to half
    # step 2: merge them
    for i in range(1,n):
        curr = dummy.next
        tail = dummy
        print('i',i,'curr',curr)
        print("--------------")
        while curr!=None:
            print("++++++++")
            left = curr
            print('left before split',left)
            right = split(left, i)
            print('left after split',left)
            print('right',right)
            curr = split(right, i)
            print('right after split',right)
            print('curr',curr)
            tail = merge(left, right, tail)
            print('tail',tail)
            print("++++++++")
    return dummy.next


def merge(h1:ListNode,h2:ListNode,prev:ListNode)->ListNode:
    '''A helper method for sortList to help merge two linked-list'''
    curr = prev
    while h1!=None and h2!=None:
        if h1.val < h2.val:
            curr.next = h1
            h1 = h1.next
        else:
            curr.next = h2
            h2 = h2.next
        curr = curr.next
    if h1!=None:
        curr.next = h1
    if h2!=None:
        curr.next = h2
    # get the tail
    while curr.next != None: curr = curr.next
    return curr

def split(head: ListNode,step:int) -> ListNode:
    '''A helper method for sortList to help split a linked-list into two parts,
    one with length step, one whatever remained.
    Modify the head node to length step, and return the head of the second ListNode
    '''
    if head == None: return head
    i=1
    while head.next!=None and i< step:
        head = head.next
        i +=1
    right = head.next
    head.next = None
    return right
    # if head == None or head.next == None: return (head, None)
    # prev = None
    # slow = fast = head
    # while fast != None and fast.next != None:
    #     prev = slow
    #     slow = slow.next
    #     fast = fast.next.next
    # prev.next = None  # disconnect the tail of first half from second half
    # return (head, slow)


def get_length(head: ListNode) -> int:
    ''' get the length of a linkedlist'''
    curr = head
    i = 0
    while curr != None:
        i += 1
        curr = curr.next
    return i


def recursive_sortList(head: ListNode) -> ListNode:
    '''
    Use merge sort (up-to-button)
    although we don't use any space in the program, each time we call recursion it still consumes
    memory in the stack frame, so the actual space complexity is O(log n) considering the recursive call.
    O (n log n) time with O(log n) space
    '''
    if not head or not head.next: return head
    # step 1: divide, split the linked list to half
    slow = fast = head
    prev = None
    while fast != None and fast.next != None:  # get the mid node
        prev = slow
        slow = slow.next
        fast = fast.next.next
        # print(prev,slow,fast)
    prev.next = None  # cut the connection of tail node in first half to the head of second half
    # step 2: sort each half, will call recursion for O(lg_2 n) times.
    h1 = recursive_sortList(head)
    h2 = recursive_sortList(slow)  # slow is the head of second half linked-list
    # step 3: merge them
    return merge_helper(h1, h2)


def merge_helper(l1: ListNode, l2: ListNode) -> ListNode:
    '''a helper method for recursive_sortList'''
    if not l1: return l2
    if not l2: return l1
    dummy = ListNode()
    prev = dummy
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    if l1 != None:  # if l1 has leftover
        prev.next = l1
    if l2 != None:  # if l2 has leftover
        prev.next = l2
    return dummy.next


def sortlist(head: ListNode) -> ListNode:
    '''
    This approach takes O(n) time and O(n) space.
    '''
    array = []
    curr = head
    while curr:
        array.append(curr.val)
        curr = curr.next
    heapq.heapify(array)
    curr = head
    while curr:
        curr.val = heapq.heappop(array)  # O(log n)
        curr = curr.next
    return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-3)
    print(head)
    # s = recursive_sortList(head)
    # print(s)
    k = sortList(head)
    print(k)
