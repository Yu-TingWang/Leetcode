'''
https://leetcode.com/problems/generate-parentheses/description/
No.22 Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
def generateParentheses(n:int)->list:
    '''
    return a list of string that are n pairs valid parentheses
    '''
    result = []
    generate(n,result,'',0,0)
    return result

'''
let say n=3
                       ε 
                    /    \
                  (       ) --> got pruned
                /   \
               (      ) 
             /   \   / \
            (    )  (    ) --> got pruned 
'''

def generate(n:int,solutions:list,curr:str,curr_left:int,curr_right:int):
    '''
    n: (global) the number of pairs
    solutions: (global)the list of string that has n pairs valid parentheses
    curr: the current str we have generated so far
    curr_left: the number of '(' in curr
    curr_right: the number of ')' in curr
    curr_left must be greater or equal to curr_right, otherwise can't form a valid parentheses
    '''
    if len(curr) > n*2: return
    if len(curr) == n*2 and curr_left == curr_right:
        solutions.append(curr)
    if curr_left<=n and curr_left >= curr_right:
        generate(n,solutions,curr+')',curr_left,curr_right+1)
        generate(n,solutions,curr+'(',curr_left+1,curr_right)

def backtrack(n:int,solutions:list,curr:str,curr_left:int,curr_right:int):
    '''
    Another way of generating, quicker than generate because we reduce redundant calls
    '''
    if len(curr) == n*2:
        solutions.append(curr)
    if curr_left < n:
        backtrack(n,curr+'(',curr_left+1,curr_right)
    if curr_right < curr_left:
        backtrack(n,curr+')',curr_left,curr_right+1)

if __name__ == '__main__':
    print(generateParentheses(3))
