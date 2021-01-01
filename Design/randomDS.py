'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
Leetcode No.380. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that
at least one element exists when this method is called). Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.map = {}  # map from element to its index in array

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:  # takes O(1)
            self.array.append(val)
            self.map[val] = len(self.map)
            # print(self.map)
            return True
        else:
            # print(self.map)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            index = self.map[val]
            if index != len(self.map) - 1:
                # swap the value at index with last value
                replaced = self.array[-1]
                self.array[index] = replaced
                self.map[replaced] = index
            self.array.pop()
            del self.map[val]
            # print(self.map)
            # big No self.array.pop(index)# this will take O(n) time
            return True
        else:
            # print(self.map)
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        length = len(self.map)
        from random import randrange
        index = randrange(length)
        return self.array[index]