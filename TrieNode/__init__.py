class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # since there are 26 letters in english
        # if node represents if the path from root to node is a word
        self.isEndOfWord = False