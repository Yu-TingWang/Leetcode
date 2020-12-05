'''
https://leetcode.com/problems/word-search-ii/description/
No.212
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be
constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

Approach:
DFS + Trie
let say
board = [                       words = ['oath','pea','eat',rain']
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
        ]
do dfs from board[0][0]:
'o' -> no up
    -> no left
    -> right is 'a' -> no up
                    -> has traversed its left
                    -> right is 'a' -> but there's no word in words has prefix 'ooa'
                    -> down is 't'  -> has traversed its up
                                    -> left is 'e' -> but theres no word in words has prefix 'oate'
                                    -> right is 'a' -> but theres no word in words has prefix 'oata'
                                    -> down is 'h' -> there is a word in words has prefix 'oath'
    --> down is 'e' -> but there is no word in words has prefix 'oe'
'''


def wordSearch(board, words) -> list:
    '''
    board: a 2d array where each cell is a letter
    words: a list of words
    '''
    result = []
    #root = construct_trie(words)
    trie = Trie()
    node = trie.root
    for word in words:trie.insert(word)
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(board,result,node,'',i,j)
    return result


from leetcode.TrieNode import Trie, TrieNode
def dfs(board,solutions,curr:dict,path:str, i, j):
    '''
    board: global from wordSearch
    curr: global constructed from words
    solutions: global, the list that contains words in board
    path: the prefix
    i, j : boars[i][j] is the current letter we are at
    '''
    if curr.isWord:
        solutions.append(path)
        curr.isWord = False
    letter = board[i][j]
    node = curr.children.get(letter)

    if not node: return
    # if letter == "#" or letter not in curr: return
    # node = curr[letter]
    # if node !={}:
    #     path += letter
    #     curr[letter] = {} # de-duplicate
    # if node =={}:
    #     solutions.append(path+letter)
    board[i][j] = "#" # mark as visited since we cannot use it twice
    path +=letter
    if i>0: dfs(board,solutions,node,path,i-1,j)
    if j>0: dfs(board,solutions,node,path,i,j-1)
    if i<len(board)-1: dfs(board,solutions,node,path,i+1,j)
    if j<len(board[0])-1: dfs(board,solutions,node,path,i,j+1)
    board[i][j] = letter # mark it back once finish
    #curr[letter] = node
    # # print board
    # print('[')
    # for i in range(len(board)):
    #     print(board[i])
    # print(']')

def TrieBuilder(word_list):
    root = Trie()
    for word in word_list:
        root.insert(word)
    return root


class TrieNode():
    def __init__(self):
        import collections
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

def construct_trie(word_list: list):
    root = {}
    for word in word_list:
        level = root
        for letter in word:
            if letter not in level: # if no previous one share prefix
                level[letter] = {}
            #print(word,'letter',letter,'level',level,'trie',root)
            level = level[letter]
    return root

if __name__ == '__main__':
    board = [['o', 'a', 'a', 'n'],
              ['e', 't', 'a', 'e'],
              ['i', 'h', 'k', 'r'],
              ['i', 'f', 'l', 'v']
            ]
    words = ['oath', 'pea', 'eat', 'rain','eathf']
    # k = construct_trie(words)
    # print(k)
    # print(k['p']['e']['a'])
    print(wordSearch(board,words))