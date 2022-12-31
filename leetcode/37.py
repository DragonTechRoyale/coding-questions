import pdb, random

def chunk(lst, n):
    ret_lst = []
    rng = len(lst) / n
    for i in range(n):
        ret_lst.append(lst[i*rng:(i+1)*rng])
    return ret_lst

# Returns True if list has unique values
def check_unique(lst):
    return len(lst) > len(set(lst))

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    rows_opts = []
    for row_idx in range(len(board)):
        row = board[row_idx]
        row_options = []
        for i in range(len(row)):
            item = row[i]
            if item == ".":
                column = []
                box = []

                for tmp_row in board:
                    column.append(tmp_row[i])
                
                small_row_idx = row_idx / 3
                small_i = i / 3
                needed_rows = board[small_row_idx*3:(small_row_idx*3)+3]
                box = [
                    chunk(needed_rows[0], 3)[small_i],
                    chunk(needed_rows[1], 3)[small_i],
                    chunk(needed_rows[2], 3)[small_i]
                ]

                print "pos: [{0}, {1}]".format(i, row_idx)
                print "column:"+str(column)
                print "box:"+str(box)

                options = []
                for j in range(1, 10):
                    j = str(j)
                    if not j in str(row) and not j in str(column) and not j in str(box):
                        options.append(j)
                row_options.append({'options':options,'chosen':options[0]})
        rows_opts.append(row_options)
        print "row_options:"+str(row_options)
    print "rows_opts:"+str(rows_opts)

                        


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)

for row in board:
    print(row)