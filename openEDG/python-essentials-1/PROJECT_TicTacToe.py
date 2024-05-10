def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    listBoard = [[0 for _ in range(25)] for _ in range(13)]
    for x in range(13):
        for y in range(25):
            if x%4==0:
                if y%8==0:
                    listBoard[x][y] = "+"
                else:
                    listBoard[x][y] = "-"
            else:
                if y%8==0:
                    listBoard[x][y] = "|"
                else:
                    listBoard[x][y] = " "
    numbers = [i for i in range(1,10)]
    for x in range(13):
        for y in range(25):
            print(listBoard[x][y], end="")
        print()


# def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.
