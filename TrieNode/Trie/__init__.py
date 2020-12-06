from leetcode.TrieNode import TrieNode
class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def __charToIndex(self, ch):
        # private helper function, converts key current character into index
        return ord(ch) - ord('a')

    def insert(self, word):
        # if not present,inserts key into trie, otherwise mark it as leaf node
        r = self.root
        length = len(word)
        for level in range(length):
            index = self.__charToIndex(word[level])
            # if curr char is not in the trie
            if not r.children[index]:
                r.children[index] = self.getNode()
            r = r.children[index]
        r.isEndOfWord = True

    def search(self, word):
        '''
        if word is a prefix in this trie
        '''
        r = self.root
        length = len(word)
        for level in range(length):
            index = self.__charToIndex(word[level])
            if not r.children[index]:
                return False
            r = r.children[index]
        return r != None and r.isEndOfWord
