'''
https://leetcode.com/problems/word-break/description/
No.139 Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
----------------
https://leetcode.com/problems/word-break-ii/
140. Word Break II
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
'''

def wordBreak(s:str,wordDict:list)->bool:
    states = [True]+[False]*len(s) # states[i] = if s[:i) can be slice into words in wordDict
    for i in range(1,len(states)):
        for j in range(i):
            if states[j] and s[j:i] in wordDict:
                states[i]=True
                # break
        # j = i
        # while j>0 and not states[j]: j-=1 # find the index of last matched word
        # substring = s[j:i]
        # states[i] = substring in wordDict
    return states[-1]

def wordBreakII(s:str,wordDict:list)->list:
    '''
    '''
    result = []
    states = wordBreak1(s,wordDict)
    words = set(wordDict)
    backtrack(s,words,states,result,0,'')
    return result


def wordBreak1(s:str,wordDict:list)->list:
    states = [True] + [False] * len(s)  # states[i] = if s[:i) can be slice into words in wordDict
    for i in range(1, len(states)):
        for j in range(i):
            if states[j] and s[j:i] in wordDict:
                states[i]=True
    return states

def backtrack(s,words,states,solu,i,curr):
    '''
    s: str, global from workdBreak
    words: list[str] , set of words from dictionary
    states: states[i] represents if s[:i) can be composed of words
    solu: result to store
    i: current index pointing on s that we re working on
    curr: current words we collect
    '''
    if states[i+len(s)]:
        if not s:
            solu.append(curr.strip())
        for j in range(1,len(states)):
            if s[:j] in words:
                backtrack(s[j:],words,states,solu,i+1,curr+''+s[i:j])



if __name__ == '__main__':
    # s = 'leetcode'
    # words = ['leet','code']
    # print(wordBreak(s,words))
    s = 'catsanddog'
    words = ['cat','cats','and','sand','dog']
    print(wordBreakII(s,words))
