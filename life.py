def surrounding_cells(board, pos_y, pos_x):     # positions run top-left to bottom right  
    
    # create list of surounding cells starting at top-left and proceding clockwise
    cell_list = [board[pos_y - 1][pos_x - 1]]

    for i in range(2):
        cell_list.append(board[pos_y - 1][pos_x + i])
    
    for i in range(2):
        cell_list.append(board[pos_y + i][pos_x + 1])

    for i in range(2):
        cell_list.append(board[pos_y + 1][pos_x - i])

    cell_list.append(board[pos_y][pos_x - 1])


    return cell_list


def run_cycle(board, pos_y, pos_x):
    current = board[pos_y][pos_x]
    count = 0   # counts number of live adjacent cells
    region = surrounding_cells(board, pos_y, pos_x)
    
    for i in region:
        if i == 1:
            count += 1

    # Any live cell with 2 or 3 live neighbors survives
    if current == 1 and count >= 2 and count < 4:
        return True

    # Any dead cell with 3 live neighbors becomes a live cell
    if current == '_' and count == 3:
        return True

    # All other live cells die in the next generation
    return False

def initialize_board(board):
    pass

def main():
    # print initial board
    board = [['_'] * 30 for i in range(30)]

    # for testing surrounding_cells()
    '''board[0][0] = 1
    board[1][0] = 8
    board[2][0] = 7
    board[2][1] = 6
    board[2][2] = 5
    board[1][2] = 4
    board[0][2] = 3
    board[0][1] = 2'''


    # for testing run_cycle
    board[10][10] = 1
    board[10][11] = 1
    board[11][10] = 1
    board[11][11] = 1

    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    
    alive = run_cycle(board, 11, 11)

    print("Alive: " + str(alive))
   # surrounding_cells(board, 1, 1) 

main()
