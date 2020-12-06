'''
Template to solve 'substring' problem

1. Use two pointers: start  & end to represent a window, use a hashmap to record pointers.
2. move end to find a valid window
3. when a valid window is found, move start to find a more qualified window, (smaller/larger depends on the problem)

int findSubstring(string s){
        vector<int> map();
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring
        for() { /* initialize the hash map here */ }

        while(end<s.size()){
            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){

                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again

                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }

            /* update d here if finding maximum*/
        }
        return d;
  }
'''


"""
https://leetcode.com/problems/minimum-window-substring/
Leetcode No.76
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""
def mindWindowSubstring(s:str,t:str):
    '''

    '''
    if not s or not t:
        return ""
    result = ""
    from collections import defaultdict
    lettercount = defaultdict(lambda :0) # maps from char in t to its frequency
    left, count , minLen = 0,0,len(s)
    for char in t:
        lettercount[char]+=1
    for right in range(len(s)):
        if s[right] in lettercount:
            lettercount[right]-=1
            if lettercount[right]==0:
                count+=1
        while count == len(t):
            if right-left+1 < minLen:
                result = s[left:right + 1]
                minLen = right-left+1
    return result

def minWindow(s:str,target:str):
    '''
    maintain a sliding window [start:i], where each char's frequency == that in T
    When char[start] has frequency > 1, move start to find the next valid window
    '''
    result = ""
    from collections import defaultdict
    mapS = defaultdict(lambda :0)
    mapT = defaultdict(lambda :0)
    for char in target: mapT[char]+=1
    count,start = 0,0
    for i,char in enumerate(s,1):
        if mapT[char] > 0:
            mapS[char] +=1
            if mapS[char] >= mapT[char]:
                count +=1
        if count == len(target):
            while mapT[s[start]] < mapS[s[start]] or mapT[s[start]]==0: # move start pointer
                if mapT[s[start]] < mapS[s[start]]: # move start to next valid window
                    mapS[s[start]] -=1
                start+=1
            if result == "" or (i-start+1) < len(result):#update result when there is a shorter one
                result = s[start:i+1]
    return result

def min_window_substring(s,t):
    '''

    '''
    from collections import Counter
    need = Counter(t) # maps from each letter in t and its frequency
    missing = len(t) # this will record the number of letter we still need to match in the current window
    start , end = 0,-1
    i = 0 #marks the start index of a valid window, before we find one, it remains 0
    for j , char in enumerate(s):
        print('-----------start loop for j=',j,'char=',char,'current window:',s[start:end+1],'-----------')
        if need[char] >0: # if char is in t
            missing -=1
        need[char] -=1
        print(need,missing)
        if missing == 0: # this line will hit when we encounter the first valid window that contains all string in t
            print('before',need,i,j)
            # print('all match',char)
            # move i to the index of next matched character,whose value should be 0 in the map need
            while i< j and need[s[i]] <0: # remove chars to find the real start
                need[s[i]] +=1
                i+=1
            need[s[i]] +=1 # make sure the first appearing char satisfies need[char] >0
            print('after',need,i)
            missing +=1 # since we remove the previous matched char, so add missing by 1
            if end == 0 or j-i < end-start+1:
                start ,end = i,j
            i+=1    # update i to start+1 for next window
    return s[start:end+1]



if __name__ == '__main__':
    s = 'adobecodebanc'
    t = 'abc'
    #print(minWindow(s,t))
    #print(mindWindowSubstring(s,t))
    print(s,t)
    print(min_window_substring(s,t))




