'''
https://leetcode.com/problems/lru-cache/
No.146

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node() # dummy pointer to head
        self.tail = Node() # dummy pointer to tail
        self.node_map = {} #maps from key to the node
        self.cap = capacity

    def get(self, key: int) -> int:
        result = -1 # if not found
        if key in self.node_map:
            node = self.node_map[key]
            result = node.val
            self.remove(node)
            self.add(node)
        return result


    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            if (len(self.node_map)==self.cap):
                del self.node_map[self.tail.prev.key]
                self.remove(self.tail.prev)
            new_node = Node(value)
            self.node_map[key] = new_node
            self.add(new_node)

    def add(self,node):
        '''
        Add the given node to the head of the list
        '''
        head_next = self.head.next # get the head node
        node.next = head_next
        head_next.prev=  node
        self.head.next = node
        node.prev = self.head

    def remove(self,node):
        ''' Remove a node from the doubly linkedlist
        '''
        next_node = node.next
        prev_node = node.prev
        next_node.prev= prev_node
        prev_node.next= next_node


class Node():

    def __init__(self,x=None,key=None):
        self.key = key
        self.val = x
        self.prev= None
        self.next = None