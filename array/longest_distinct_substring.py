"""
Find the length of longest substring without duplication
No.3 Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def lengthOfLongestSubstring(s:str)->int:
    """
    Using sliding window
    return the length of longest substring without duplication
    """
    appeared=set() # record what have appeared
    curr_longest =0 # the lenght of the current longest substring
    i = 0 # current pointer
    j = 0 # points to the start index of the current longest substring
    # goal : maximize curr_longest, namely [j:i]
    while i< len(s) and j<len(s):
        #print('j',j,'i',i,appeared,'curr',curr_longest,'s[j:i]',s[j:i])
        if s[i] not in appeared:
            appeared.add(s[i]) # add this to our record
            i+=1
            # why update i before update curr_longest ???
            # --> to get the length, we have to do |s[j:i']| where i' = i+1
            curr_longest = max(curr_longest,i-j)
        else:
            appeared.remove(s[j]) # since s[i] has appeared, s[j:i] no longer qualify as distinct substring
            # remove it and update the pointer at start index of curr longest substring
            j+=1
    print(i,j,s[j:i])
    return curr_longest

def lengthMap(s:str)->int:
    """
    optimized sliding window
    Using sliding window+dictionary
    """
    map={} # letter(key) maps to index (value)
    i=0 # the start index of the current longest distinct substring
    result=0 # the length of the current longest distinct substring
    for j in range(len(s)):
        print('s[j]',s[j],'i',i,map,'result',result)
        if s[j] in map:
            i = max(map[s[j]],i)
        result = max(result,j-i+1)
        map[s[j]] = j+1
    return result



if __name__ == '__main__':
    s = "helloworld"
    print(lengthOfLongestSubstring(s))
    print(lengthMap(s))

