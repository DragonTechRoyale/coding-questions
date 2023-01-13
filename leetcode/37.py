import pdb, random, sys
from math import floor

sys.setrecursionlimit(0xfffffff)

__TRUE_SUDOKU = (9, 9)


def chunk(lst, n):
    ret_lst = []
    rng = len(lst) // n
    for i in range(n):
        ret_lst.append(lst[i*rng:(i+1)*rng])
    return ret_lst


# Returns True if list has unique values
def check_unique(lst):
    return len(lst) > len(set(lst))


def get_columns(board):
    columns = []
    for i in range(9):
        clmn = []
        for row in board:
            clmn.append(row[i])
        columns.append(clmn)
    
    return columns


def get_boxes(board):
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
    
    return boxes


# Takes an index of the box and returns a list of vectors of that box
def get_box_vectors(box_idx: int) -> list:
    rank_idx = box_idx // 3 
    stack_idx = round((box_idx/3 % 1) * 3)

    start_row_idx = rank_idx * 3
    start_column_idx = stack_idx * 3

    start_vec = (start_row_idx, start_column_idx)
    vectors = [start_vec]*9

    for i in range(9):
        vec = vectors[i]
        row_idx, column_idx = vec

        if i % 2 == 0:
            column_idx += 1
        elif i % 3 == 0:
            column_idx += 2
        
        row_idx += floor(i/3)
    
        new_vec = (row_idx, column_idx)
        vectors[i] = new_vec
        
    return vectors



def isValidSudoku_vector(board): # returns a vector of the faulty one, if not found then returns (9, 9)
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check rows
    for row_idx in range(len(board)):
        row = board[row_idx]
        for item_idx in range(9):
            item = row[item_idx]
            if item != "." and row.count(item) > 1:
                return (row_idx, item_idx)
    
    # Create columns
    columns = get_columns(board=board)

    # Check columns
    for column_idx in range(9):
        clmn = columns[column_idx]
        for row_idx in range(9):
            item = clmn[row_idx]
            if item != "." and clmn.count(item) > 1:
                return (row_idx, column_idx)

    # Create 3x3's
    boxes = get_boxes(board=board)

    # Check 3x3's
    for box_idx in range(9):
        bx = boxes[box_idx]

        for box_index in range(9):
            item = boxes[box_index]

            if item != "." and bx.count(item) > 1:
                return get_box_vectors(box_idx=box_idx)[box_index]

    return __TRUE_SUDOKU


def isValidSudoku(board: list) -> bool:
    return isValidSudoku_vector(board=board) == __TRUE_SUDOKU


def create_rand_list(needed_items):
    rand_list = []

    for i in range(needed_items):
        rand_list.append(str(random.randrange(1,10,1)))
    
    return rand_list


def dup_board(board):
    new_board = []
    for row in board:
        new_row = []
        for item in row:
            new_row.append(item)
        new_board.append(new_row)
    return new_board


def apply_items(optional_items, board):
    tmp_board = dup_board(board)

    for i in range(9):
        for j in range(9):
            if tmp_board[i][j] == ".":
                tmp_board[i][j] = optional_items.pop()
    
    return tmp_board


def apply_rows_opts(rows_opts, board):
    tmp_board = dup_board(board)

    for i in range(9):
        for j in range(9):
            if tmp_board[i][j] == ".":
                if not rows_opts:
                    continue
                if not rows_opts[i]:
                    continue
                curr_opt = rows_opts[i].pop(0)['chosen']
                tmp_board[i][j] = curr_opt
    
    return tmp_board


def shuffle_rows_opts(rows_opts):
    new_rows_opts = dup_board(rows_opts)
    for i in range(len(new_rows_opts)):
        for j in range(len(new_rows_opts[i])):
            new_rows_opts[i][j]['chosen'] = random.choice(new_rows_opts[i][j]['options'])

    return new_rows_opts


def print_board(board):
    print('-'*45)
    for row in board:
        print(row)


def print_changed_vec(board, vec):
    if vec != (9,9):
        board = dup_board(board)
        board[vec[0]][vec[1]] = f"*{board[vec[0]][vec[1]]}*"
    print_board(board)


def get_by_vector(row_idx: int, column_idx: int, board: list):
    new_board = dup_board(board=board)

    row = new_board[row_idx]

    columns = get_columns(board=new_board)
    stacks = get_stacks(board=new_board)

    row = new_board[row_idx]
    column = columns[column_idx]

    rank_idx = row_idx//3
    stack_idx = column_idx//3
    box = stacks[stack_idx][rank_idx]

    return row, column, box


def get_stacks(board: list) -> list:
    new_board = dup_board(board=board)
    boxes = get_boxes(board=new_board)

    stacks = []
    for stack_idx in range(3):
        stck = []
        for rank_idx in range(3):
            stck.append(boxes.pop(0))
        stacks.append(stck)
    
    return stacks


def solveSudoku(board):
    return solveSudoku_func(board=board,changed_vecs=[])


def solveSudoku_func(board, changed_vecs,i=1):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """

    print(changed_vecs)
    if changed_vecs:
        print_changed_vec(board=board,vec=changed_vecs[-1])
    else:
        print_board(board)

    if not '.' in str(board):
        return True

    columns = get_columns(board=board)
    stacks = get_stacks(board=board)

    for row_idx in range(9):
        row = board[row_idx]
        for column_idx in range(9):
            column = columns[column_idx]
            item = board[row_idx][column_idx]
            
            if not item == '.':
                continue 

            rank_idx = row_idx//3
            stack_idx = column_idx//3
            box = stacks[stack_idx][rank_idx]

            key = (row_idx, column_idx)
            opts = []

            board[row_idx][column_idx] = str(i)
            if isValidSudoku(board):
                changed_vecs.append((row_idx, column_idx))
                return solveSudoku_func(board=board, changed_vecs=changed_vecs, i=1)
            
            i += 1

            board[key[0]][key[1]] = '.'
            '''
            if changed_vecs:
                vec_last = changed_vecs.pop()
                board[vec_last[0]][vec_last[1]] = '.'
            
            if changed_vecs:
                vec_before = changed_vecs.pop()
                board[vec_before[0]][vec_before[1]] = '.'
                '''
            return solveSudoku_func(board=board, changed_vecs=changed_vecs, i=i)



board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(board))

print_board(board=board)