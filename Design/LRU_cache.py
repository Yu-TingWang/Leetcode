'''
https://leetcode.com/problems/lru-cache/
No.146

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.queue = []
        self.curr_size = 0

    def get(self, key: int) -> int:
        # each time when i get a key, i move it to the front of the queue
        if key not in self.map:
            # print(self.map,self.queue,self.cap,self.curr_size)
            return -1
        else:
            val = self.map[key]
            index = self.queue.index(key)
            self.queue.pop(index)
            self.queue.insert(0, key)
            # print(self.map,self.queue,self.cap,self.curr_size)
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            index = self.queue.index(key)
            self.queue.pop(index)
            self.queue.insert(0, key)
            self.map[key] = value
        else:
            if self.curr_size == self.cap:
                least_used = self.queue.pop()
                del self.map[least_used]
                self.curr_size -= 1
            self.queue.insert(0, key)
            self.map[key] = value
            self.curr_size += 1

