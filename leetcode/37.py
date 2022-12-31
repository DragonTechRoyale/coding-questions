import pdb 
import itertools

def chunk(lst, n):
    ret_lst = []
    rng = len(lst) / n
    for i in range(n):
        ret_lst.append(lst[i*rng:(i+1)*rng])
    return ret_lst

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """

    # create ranks and stacks
    ranks = []
    stacks = []
    columns = []

    for i in range(3):
        curr_rank = board[i*3:(i*3)+3]
        tmp_rank = []
        for row in curr_rank:
            row = chunk(row, 3)
            tmp_rank.append(row)
        ranks.append(tmp_rank)

    print "ranks:"
    for rank in ranks:
        for row in rank:
            print row
    
    for i in range(9):
        curr_column = []
        for row in board:
            curr_column.append(row[i])
        columns.append(curr_column)
    
    print "columns:"
    for column in columns:
        print column
    
    for i in range(3):
        stacks.append(list(columns[i*3:(i*3)+3]))

    print "stacks:"
    for stack in stacks:
        print stack

    # do rank scanning
    for rank_idx in range(len(ranks)):
        curr_rank = ranks[rank_idx]
        for block_idx in range(len(curr_rank)):
            curr_block_row = 


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print "start board:"
for row in board:
    print(row)

solveSudoku(board)

print "end board:"
for row in board:
    print(row)