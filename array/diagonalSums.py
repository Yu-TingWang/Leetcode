"""
https://leetcode.com/problems/matrix-diagonal-sum/submissions/
No.1752
Compute the diagonal Sum
"""
def diagonalSum(matrix):
    """
    matrix, list[list[int]]
    """
    sums = 0
    n = len(matrix)
    for i in range(n):
        for j in {i,n-i-1}:
            sums += matrix[i][j]
    return sums
    # return sum(sum(m[j] for j in {i,len(matrix)-i-1}) for i, m in enumerate(matrix))
