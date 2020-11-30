"""
Find the length of longest palindrome substring
No.5
https://leetcode.com/problems/longest-palindromic-substring/
"""

def brute_force(s:str):
    """
    The most straightforward method, get all the possible substring,
    verify if it is palindrome, and update the current maximum length.
    there are C(n,2) substrings, so it will take O(n^2) to find all substrings, and verifying each takes O(n).
    So this approach will take O(n^3) time.
    but O(1) space complexity
    """
    curr_max=0
    curr_long = ''
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            tmp = s[i:j]
            #print(tmp,i,j)
            if tmp == tmp[::-1]:
                if len(tmp)>curr_max:
                    curr_long = tmp
                    curr_max = len(tmp)
    return curr_long

def expand_center(s:str):
    """
    Since each palindrom mirrors around its center, hence if we try to expanded it from a center, we can get palindrom s
    string, and there are only 2n-1 such center.
    --> why 2n-1 ? because the center of palindrome can be in between to character. ex. 'abba' the center is ab|ba
    So n(each letter) + (n-1) the cap between two letter (empty string, but just view it as location)
    So we have two cases of palindrome,
    Case 1.'baab' where each character has a match
    Case 2.'racecar' the center does not has match, but this is still a palindrome
    Time Complexity = O(n) * O(2n-1) = O(n^2)
    Space Complexity = O(1) just a few pointers are used, only take constant space.
    """
    if s==None or len(s)<1: return ''
    start=0
    end=0
    for i in range(len(s)): # this takes O(n)
        # calling the helper function takes O(n) times
        len1 = expandFromMid(s,i,i+1) # case1
        len2 = expandFromMid(s,i,i)  # case 2, so the first iteration will check the same exact character
        max_len = max(len1,len2)
        if max_len > end-start:# i is the center
            start = i - (max_len-1)//2 # so we need to substract half of the length to get the start index
            end = i + (max_len)//2
    return s[start:end+1]

def expandFromMid(s:str,left:int,right:int)->int:
    """
    the left,right index is the index of center, and we are trying to maximize |right-left|
    Return the length of the palindrome that we found
    a helper method for expand center
    """
    if s ==None or left>right:
        return 0
    # as long as s[left:right) is palindrome, we will remain in the loop, hence keep expanding
    while left>=0 and right < len(s) and s[left]==s[right]:
        left -=1
        right +=1
    return right-left-1


def dp(s:str):
    '''
    dynamic programming approach
    '''
    states=[[]]
    # states[i][j] True if s[i:j) is a palindrome
    # states[i][j] = states[i+1][j-1] , if s[i] == s[j]
    #              = False            , otherwise
if __name__ == "__main__":
    s='racecar'
    k='aabbcd'
    print(brute_force(s))
    print(brute_force(k))
    print(expand_center(s))
    print(expand_center(k))