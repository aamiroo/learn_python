import sys
import random

board = ["" for _ in range (9)]
win = [[0,1,2],
           [3,4,5],
           [6,7,8],
           [0,4,8],
           [1,4,7],
           [2,4,6],
           [2,5,8],
           [0,3,6]]
print ("select your mode:")
print()
your_mode = input("1: one player \n2: two player\n3: exit\n\n")
print()
try:
    if your_mode.isdigit():
        your_mode = int(your_mode)
    if (your_mode <1 or your_mode >3):
            print("Please choose correctly \n you must choice 1 or 2")
    if your_mode == 3:
        sys.exit()
except:
    print("Please do the right thing.")
player1 = "X"
player2 = "O"


while True:

    def nama ():
        
        print (f"{board[0]}    |   {board[1]}   |   {board[2]}")
        print("----+------+----")
        print (f"{board[3]}    |   {board[4]}   |   {board[5]}")
        print("----+------+----")
        print (f"{board[6]}    |   {board[7]}   |   {board[8]}")
    nama()
    
    print()
    try:

        def two ():

            your_choice = int (input(f"please enter your num for {player1}: "))
            if your_choice < 1 or your_choice > 9:
                print("Choose a number between 1 and 9")
                return
            if board[your_choice - 1] != "":
                print("This position is already occupied")
                return
            board[your_choice - 1] = "X"
                

            your_choice = int (input(f"please enter your num for {player2}: "))
            if your_choice < 1 or your_choice > 9:
                print("Choose a number between 1 and 9")
                return
            if board[your_choice - 1] != "":
                print("This position is already occupied")
                return
            board[your_choice - 1] = "O"
                
            
        def one ():
            
            your_choice = int (input(f"please enter your num for {player1}: "))
            
            if your_choice < 1 or your_choice > 9:
                print("Choose a number between 1 and 9")
                

            if board[your_choice - 1] != "":
                print("This position is already occupied")
                return
            board[your_choice - 1] = "X"
            
            while True:
                computer_valiu = random.randint(1,9)
                computer_choice = int(computer_valiu)
                if board[computer_choice - 1] == "":
                    board[computer_choice - 1] = "O"
                return


        def check_winner():
            for a, b, c in win:
                if board[a] == board[b] == board[c] != "":
                    return board[a]
            return None
        if your_mode == 1:
            one()
        if your_mode == 2:
            two()
    except:
        print("Please do the right thing.")

    winner = check_winner()

    if winner == "X":
        print("Player X wins!")
        break

    elif winner == "O":
        print("Player O wins!")
        break
    if "" not in board:
        print("Draw!")
        break
   # nama()
