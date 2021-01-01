class TrieNode():
    def __init__(self):
        self.isWord = False
        from collections import defaultdict
        # we don't need to apply lambda here because TrieNode will return something already
        self.children = defaultdict(TrieNode)
'''
why use defauldict ?
if we use defaultdict.get(key) and key is not in the dictionary, then it is going to return None,
so we use get method in search and startsWith.
if we use defaultdict[key] and key is not in the dictionary, then it is going to create a 
key with default value.
'''


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str):
        '''
        insert word into the trie
        '''
        node = self.root
        for w in word:
            # why we use [w] in stead of .get(w)?
            node = node.children[w]
        node.isWord = True

    def search(self,word:str):
        '''
        find out if word is in trie
        '''
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

    def startsWith(self,word:str):
        '''
        find ouf if word is prefix for any word in the trie
        '''
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return True

def TrieBuilder(word_list):
    root = Trie()
    for word in word_list:
        root.insert(word)
    return root

if __name__ == '__main__':
    #t = TrieBuilder(['apple','app'])
    t = Trie()
    t.insert('apple')
    print('app',t.search('app'),t.startsWith('app'))
    print('apple',t.search('apple'),t.startsWith('apple'))
    #k = Trie()Trie
    k = TrieBuilder(['h'])
    # print(k.search('hi'))


