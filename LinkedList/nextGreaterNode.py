from leetcode.LinkedList import ListNode,linkedList_builder
"""
Return the next larger value of a node.
If there is no a larger node, than put 0.

LeetCode N0.1019
https://leetcode.com/problems/next-greater-node-in-linked-list/
"""


def nextLargerNodes(head: ListNode) ->list:
    result = []
    stack = [] # take advantage of the LIFO feature of stack
    i = 0
    while head:
        result.append(0)  # the default value is 0
        # if stack is empty, then we reach the end of the linkedList
        print(i,head,stack)
        while stack and stack[-1][1] < head.val:
            print('i=',i,'stack=',stack,'result=',result)
            change = stack.pop()
            # then head.val is change[0]'s larger node ( until get the closet larger )
            result[change[0]] = head.val
        # when exit the loop, for all nodes in stack, node.nextLargerNode has been set
        # put ( index, value ) to stack
        stack.append((i, head.val))
        i += 1
        head = head.next
    return result

if __name__ == '__main__':
    head = linkedList_builder([2,1,5,7,4])
    print(nextLargerNodes(head))