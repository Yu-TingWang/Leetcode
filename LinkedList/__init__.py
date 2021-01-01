class ListNode:
    def __init__(self, x=0):
         self.val = x
         self.next = None


    def __str__(self):
        array="["
        while self!=None:
            array += str(self.val) + ","
            self=self.next
        array = array[:-1] + "]"
        return array

# class LinkedList:
#
#     def __init__(self,input:list):
#         dummy_head = ListNode()
#         curr = dummy_head
#         for i in range(len(input)):
#             curr.next = ListNode(input[i])
#             curr = curr.next
#         self = dummy_head.next
#         #return dummy_head.next
#
#     def __str__(self):
#         super(ListNode,self).__str__()

def linkedList_builder(input:list)->ListNode:
    dummy_head = ListNode()
    curr = dummy_head
    for i in range(len(input)):
        curr.next = ListNode(input[i])
        curr = curr.next
    return dummy_head.next
if __name__ == "__main__":
    l = ListNode(0)
    print(l)
    k = ListNode()
    print(k)
    p = [0,1,2,3]
    # i = LinkedList(p)
    i = linkedList_builder(p)
    print(i)
