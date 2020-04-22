"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Ex.                 After Capture:
X X X X             X X X X
X O O X             X X X X
X X O X             X X X X
X O X X             X O X X

LeetCode No.130

https://leetcode.com/problems/surrounded-regions/
"""

def capture(board:list)->list:
    """
    Flip all o to X that is surrounded by X.
    :param board: list[list[str]]
    :return: list[list[str]]
    """
    # mark all O that is not surrounded by X as B, which always starts from the border
    rows=len(board)
    columns=len(board[0])
    for i in range(rows):
        for j in range(0,columns,columns-1):
            print('capture',i,j)
            if board[i][j]=='O':
                print('capture1',i,j)
                flip(board,i,j)
    for i in range(0,rows,rows-1):
        for j in range(columns):
            if board[i][j]=='O':
                print('capture2',i,j)
                flip(board,i,j)
    # for those O remains on the board, they must be surrounded by X, so capture them
    for i in range(rows):
        for j in range(columns):
            if board[i][j]=="O": # flip to X
                board[i][j]="X"
    # now flip all B back to O
    for i in range(rows):
        for j in range(columns):
            if board[i][j]=="B":
                board[i][j]="O"
    return board
def flip(board:list,i:int,j:int)->None:
    """
    Flip all the O that is not surrounded by x to B
    :param board: list[list[str]]
    :param i: int
    :param j: int
    :return: None
    """
    if i>=0 and i<len(board) and j>=0 and j<len(board) and board[i][j]=="O":
        board[i][j]="B"
        flip(board,i,j-1)
        flip(board,i,j+1)
        flip(board,i-1,j)
        flip(board,i+1,j)

if __name__ == "__main__":
    grid = [["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]]
    flipped = capture(grid)
    for i in range(len(flipped)):
        print(flipped[i])

    bord = [["X", "X", "X", "O", "X"],
            ["X", "O", "O", "X", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "X"]]

    board_flip = capture(bord)

    for i in range(len(board_flip)):
        print(board_flip[i])