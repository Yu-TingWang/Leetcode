class Node():
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

    def __str__(self):
        root = self
        result = []
        if root == None:
            return result
        queue = []
        queue.append(root)
        while queue != []:
            size = len(queue)
            curr_level = []
            for i in range(size):
                curr = queue.pop(0)
                if curr!=None:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    curr_level.append(curr.val)
                else:
                    curr_level.append(None)
            result.append(curr_level)

        return str(result)