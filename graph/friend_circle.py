"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then
the ith and jth students are direct friends with each other, otherwise not. And you have to output the total
number of friend circles among all the students.

LeetCode No.547

https://leetcode.com/problems/friend-circles/
"""

def count_circle(friends:list)->int:
    """
    Given the relationship of i people, return the total number of friend cycle
    :param friends: list[list[int]] . friends[i][j]==1 iff i, j are direct friend.
    :return: number of friend cycle
    """
    circle=0
    visited = [False]*len(friends)
    # find the first pair of direct friends, and traverse all i's direct friend and j's direct friend
    # since friends must be symmetric, only deal with the upper triangle
    for i in range(1,len(friends)):
       if not visited[i]:# if not yet visited
           dfs(friends,visited,i)
           circle+=1
    return circle


def dfs(friends:list,visited:list,i:int):
    for j in range(len(friends)):
        # if i and j are direct friends and not yet visited
        if friends[i][j]==1 and not visited[j]:
            visited[j]=True # mark as visited
            dfs(friends,visited,j)


if __name__ =="__main__":
    friends = [[1,1,0],
               [1,1,0],
               [0,0,1]]
    friend = [[1,1,0],
              [1,1,1],
              [0,1,1]]
    print(count_circle(friends))
    print(count_circle(friend))