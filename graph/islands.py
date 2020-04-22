"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

LeetCode No.200
https://leetcode.com/problems/number-of-islands/
"""
def numIslands(grid:list) -> int:
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=="1":
                check(grid,i,j)
                total+=1
    return total

def check(grid:list,i:int,j:int):
    # run until the edge of the grid                   # dfs call until encounter a water again
    if i>=0 and i<len(grid) and j >=0 and j<len(grid[0]) and grid[i][j]=="1":
        # mark it as visited
        grid[i][j]='0'
        # dfs check
        check(grid,i,j+1)
        check(grid,i+1,j)
        check(grid,i-1,j)
        check(grid,i,j-1)


if __name__ == '__main__':
    grid=[["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
    gri= [["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]]
    print(numIslands(grid=grid))
    print(numIslands(grid=gri))

