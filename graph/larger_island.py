"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1. After, what is the size of the largest island? (An
island is a 4-directionally connected group of 1s).


LeetCode No.827
https://leetcode.com/problems/making-a-large-island/
"""

def largest_island(grid:list)->int:
    """
    Given that we can only change a 0 to 1, return the area of the largest island after me make the change
    :param grid: list[list[int]] , the 2D map representing island and land
    :return: int, the area of the island after changing
    """
    # simply connect two islands will make a larger one.
    max_area=0
    rows=len(grid)
    col = len(grid[0])
    hasZero= False
    for i in range(rows):
        for j in range(col):
            if grid[i][j]==0:
                grid[i][j]=1
                inner = [None for i in range(col)]
                visited = [inner for i in range(rows)]
                max_area = max(max_area,dfs(grid,i,j,visited))
                if max_area == rows*col:return max_area
                grid[i][j]=0
                hasZero=True
    return max_area if hasZero else rows*col


def dfs(grid:list,i:int,j:int,visited:list):
    """
    :param grid: list[list[int]] ,the 2D map representing island and land
    :param i: int , row number
    :param j: int , column number
    :param visited: list[list[boolean]] , record if grid[i][j] has been visited
    :return: int
    """
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j]==0 or visited[i][j]:
        return 0
    else:
        visited[i][j]=True
        result = 1 + dfs(grid,i-1,j,visited)+dfs(grid,i+1,j,visited)+dfs(grid,i,j-1,visited)+dfs(grid,i,j+1,visited)
        return result