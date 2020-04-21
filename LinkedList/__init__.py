class ListNode:
    def __init__(self, x=None):
         self.val = x
         self.next = None

    def __str__(self):
        array="["
        while self:
            array += str(self.val) + ","
            self=self.next
        array = array[:-1] + "]"
        return array
