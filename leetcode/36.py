# https://leetcode.com/problems/valid-sudoku/

#from __future__ import division

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check rows
    for row in board:
        for item in row:
            if item != "." and row.count(item) > 1:
                return False
    
    # Create columns
    columns = []
    for i in range(9):
        clmn = []
        for row in board:
            clmn.append(row[i])
        columns.append(clmn)

    # Check columns
    for clmn in columns:
        for item in clmn:
            if item != "." and clmn.count(item) > 1:
                return False

    # Create 3x3's
    boxes = [] # 3x3 = box
    for i in range(1, 4): # i = stack counter
        for j in range(1, 4): # j = rank counter
            bx = [] # current box

            if j == 2:
                pass
            for row_idx in range(1, 10):
                # check if row belongs to the current box
                row = [] # row of the current box
                relationship = float(j) / float(row_idx)
                desired_max = 3*j 
                is_current_row = relationship in [float(j)/float(desired_max), float(j)/float(desired_max-1), float(j)/float(desired_max-2)] 
                if is_current_row:
                    
                    # check if column belongs to current box
                    for item_idx in range(1, 10):
                        relationship = float(i) / float(item_idx)
                        desired_max = 3*i
                        is_current_item = relationship in [float(i)/float(desired_max), float(i)/float(desired_max-1), float(i)/float(desired_max-2)] 

                        if is_current_item:
                            row.append(board[row_idx-1][item_idx-1])
                
                if row:
                    bx += row

            boxes.append(bx)

    # Check 3x3's
    for bx in boxes:
        for item in bx:
            if item != "." and bx.count(item) > 1:
                return False

    return True

'''
# True
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

# False in top left 3x3
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["1",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

# False in leftest column
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","1",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

# True
board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
'''
# True
board = [
        [".","9",".",".","4",".",".",".","."],
        ["1",".",".",".",".",".","6",".","."],
        [".",".","3",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".","7",".",".",".",".","."],
        ["3",".",".",".","5",".",".",".","."],
        [".",".","7",".",".","4",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".","7",".",".",".","."]]

print(isValidSudoku(board))
