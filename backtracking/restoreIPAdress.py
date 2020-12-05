'''
https://leetcode.com/problems/restore-ip-addresses/description/
No.93
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s.
You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255,
separated by single dots and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312"
and "192.168@1.1" are invalid IP addresses.
'''

'''
Given s = '2552551135'
                (ε)
        /         /   |     \
       2         25   255   2552 -> this node get pruned cuz its more than three digits, so it wouldn't be valid
    /  |  \     / | 
   5   52 525  5  52
           |
         this node get pruned cuz its greater than 255
'''


def restoreIPAdress(s: str) -> list:
    '''
    Return a list of string that are valid IP address
    '''
    result = []
    restoreIp(s, result, 0, '', 0)
    return result


def restoreIp(ip: str, solutions: list, index: int, restored: str, count: int):
    '''
    Helper method to prune, modify solutions, return nothing
    ip: (global) The string of IP address
    solutions: (global) the list contain all valid IP address
    index: (local) the current index we are at ip
    restored: (local) the string of root-curr path
    count: (local) how many integer we have found for this potential valid address *** not count for solutions element
    '''
    # print('index',index,'resotred',restored,'count',count)
    if count > 4:
        return
    if count == 4 and index == len(ip):
        solutions.append(restored)
    for i in range(1, 4):
        # print('----')
        # print('i',i,'index',index,'restored',restored)
        if index + i > len(ip):  # since index exceed the string, no need to traverse
            break
        s = ip[index:index + i]
        if (len(s) > 1 and s[0] == '0') or (
                i == 3 and int(s) >= 256):  # leading zeros or greater than 255, not valid address
            # print('s',s)
            # print('-----')
            continue  # prune this node
        update_restore = restored + s
        if count != 3:
            update_restore += '.'
        restoreIp(ip, solutions, index + i, update_restore, count + 1)
        # print('-----')


if __name__ == '__main__':
    s = '25525511135'
    print(restoreIPAdress(s))
