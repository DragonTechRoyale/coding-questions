import pdb, random


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

        rank_idx = box_idx // 3 
        stack_idx = round((box_idx/3 % 1) * 3)

        for box_index in range(9):
            item = boxes[box_index]
            
            row_idx = # TODO calculate indexes here
            column_idx = 

            if item != "." and bx.count(item) > 1:
                return False

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
    for row in board:
        print(row)


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


def apply_options(board: list, options: dict) -> list:
    new_board = dup_board(board=board)

    keys = list(options.keys())
    random.shuffle(keys)

    for key in keys: 
        row_idx, column_idx = key
        opts = options[(row_idx, column_idx)] 
        random.shuffle(opts)

        row, column, box = get_by_vector(row_idx=row_idx, column_idx=column_idx, board=new_board)

        did_assign = False
        while not did_assign:
            for i in opts:
                if not i in row and not i in column and not i in box:
                    new_item = i
                    did_assign = True
                    break
            if not did_assign:
                # then change random value in (randomally) wither the box, column or row, so that the new board stays valid
                tmp_board = dup_board(new_board)
                while True:
                    to_change = random.choice(['row', 'column', 'box'])
                    idx_to_change = random.randrange(0, 9)
                    did_assign_new = False
                    if to_change == 'row':
                        for i in range(1, 10):
                            i = str(i)
                            new_row, new_column, new_box = get_by_vector(row_idx=row_idx, column_idx=idx_to_change, board=new_board)
                            new_key = (row_idx, idx_to_change)
                            if not i in row and not i in new_column and not i in new_box and new_key in keys:
                                tmp_board[row_idx][idx_to_change] = i
                                did_assign_new = True
                                if not isValidSudoku(tmp_board):
                                    raise Exception(f"Invalid assignment at {isValidSudoku_vector(board=board)}")
                                break
                    elif to_change == 'column':
                        for i in range(1, 10):
                            i = str(i)
                            new_row, new_column, new_box = get_by_vector(row_idx=idx_to_change, column_idx=column_idx, board=new_board)
                            new_key = (idx_to_change, column_idx)
                            if not i in new_row and not i in column and not i in new_box and new_key in keys:
                                tmp_board[idx_to_change][column_idx] = i
                                did_assign_new = True
                                if not isValidSudoku(tmp_board):
                                    raise Exception(f"Invalid assignment at {isValidSudoku_vector(board=board)}")
                                break
                    #elif to_change == 'box':
                    print('============')
                    print_board(tmp_board)
                    if did_assign_new:
                        if isValidSudoku(tmp_board):
                            break
                        else:
                            raise Exception(f"Invalid assignment at {isValidSudoku_vector(board=board)}")
                new_board = tmp_board

                
        
        if not did_assign:
            return new_board
            #raise Exception("Didn't do assignment")

        new_board[row_idx][column_idx] = new_item 
        if not isValidSudoku(new_board):
            pass
            raise Exception("Invalid assignment")

    return new_board


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


'''
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    needed_items = 0
    for row in board:
        needed_items += row.count(".")

    while True:
        optional_items = create_rand_list(needed_items=needed_items)
        new_board = apply_items(optional_items=optional_items, board=board)
        print('----------')
        print_board(new_board)
        if isValidSudoku(new_board):
            return new_board
'''
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    columns = get_columns(board=board)
    stacks = get_stacks(board=board)

    options = {} # hash table of options for items, key is indexes and value is options {(row_idx, column_idx) : ["1", "3", ...], ...}

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

            for i in range(1, 9+1):
                i = str(i)
                if not i in row and not i in column and not i in box:
                    opts.append(i)
            
            options[key] = opts
    
    while True:
        new_board = apply_options(board=board, options=options)
        print_board(new_board)
        print("----------------")
        if isValidSudoku(new_board) and not '.' in str(new_board):
            return new_board
            break

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

print_board(board=board)