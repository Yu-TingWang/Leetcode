"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

https://leetcode.com/problems/search-a-2d-matrix/
LeetCode No.74
"""


def searchMatrix(matrix:list,target:int)->bool:
    """

    :param matrix: list[list[int]]. a 2d array
    :param target: int, the target number to be searched
    :return: if the target number is in the matrix
    """
    if not matrix :return False
    # find which row the target will possibly be
    start_row=0
    end_row = len(matrix)
    while start_row<end_row:
        mid = (start_row+end_row)//2
        if target>=matrix[mid][0] and target<=matrix[mid][len(matrix[mid])-1]:
            start_row=mid
            break
        elif target<=matrix[mid][0]:
            end_row=mid-1
        else:
            start_row=mid+1
    row=start_row
    # search on the row
    start = 0
    end = len(matrix[row]) - 1
    while start <= end:
        mid = (start + end) // 2
        if matrix[row][mid] == target:
            return True
        if matrix[row][mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False