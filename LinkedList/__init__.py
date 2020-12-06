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

if __name__ == "__main__":
    l = ListNode(0)
    print(l)
    k = ListNode()
    print(k)
    p = [0,1,2,3]
    i = ListNode(p)
    print(i)