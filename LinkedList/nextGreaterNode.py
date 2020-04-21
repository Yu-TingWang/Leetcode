from LinkedList import ListNode
"""
Return the next larger value of a node.
If there is no larger node, than put 0.
"""
def nextLargerNodes(head: ListNode) ->list[int]:
    result = []
    stack = []
    i = 0
    while head:
        result.append(0)
        while stack and stack[-1][1] < head.val:
            change = stack.pop()
            result[change[0]] = head.val
        stack.append((i, head.val))
        i += 1
        head = head.next
    return result