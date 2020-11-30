"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
No.345
"""
def reverseVowels(s:str)->str:
    """
    Use two lists,
    indices to store the index who is a vowel,
    vowels to store the vowel appeared backward
    """
    indices=[]
    vowels=[]
    v = set('aeiouAEIOU')
    for i in range(len(s)):
        if s[i] in v:
            indices.append(i)
            vowels.insert(0,s[i])
    l=list(s)
    for i in range(len(indices)):
        l[indices[i]]=vowels[i]
    return ''.join(l)

def reverseVowels_ptr(s:str)->str:
    """
    Use two pointer, one traverse from front and one from back
    Finish traversing once front pointer has passed back pointer
    """
    l=list(s)
    vowels=set('aeiouAEIOU')
    front = 0
    back = len(s)-1
    while front < back:
        print(front,back)
        if l[front] in vowels:
            if l[back] in vowels:
                tmp = l[back]
                l[back] = l[front]
                l[front] = tmp
                front+=1
            back -=1
        else:
            front +=1
            if l[back] not in vowels:
                back-=1
    return ''.join(l)




if __name__ == '__main__':
    s = 'hello'
    print(reverseVowels_ptr(s))
