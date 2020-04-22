"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

LeetCode No.695
https://leetcode.com/problems/max-area-of-island/

"""

def maxAreaOfIsland(grid:list) ->int:
    """
    get the max area of island in the grid
    """
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                max_area = max(max_area,compute_area(grid,i,j))
    return max_area

def compute_area(grid:list,i:int,j:int) -> int:
    """
    compute the area of an island
    """
    if i>=0 and i< len(grid) and j>=0 and j<len(grid[i]) and grid[i][j]==1:
        # mark as visited
        grid[i][j]=0
        return 1 + compute_area(grid,i,j-1)+compute_area(grid,i,j+1)\
               +compute_area(grid,i-1,j)+compute_area(grid,i+1,j)
    else:
        return 0

if __name__ == '__main__':
    grid = [[ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ],
            [ 0 , 1 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
            [ 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 ],
            [ 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ],
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ],
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ]]

    print(maxAreaOfIsland(grid=grid))
