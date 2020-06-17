#This is a two player pygame Tic tac toe

def user_select():
    global players
    select = ""
    while select != "O" and select != "X":
        select = input("Player 1: select either O or X")
    #else: print("Value entered not supported")
    if select == "X":
        players = ("X","O")
    else: players = ("O" , "X")
    return players





def board(row1,row2,row3):
    print("===============")
    print(row1)
    print("===============")
    print(row2)
    print("===============")
    print(row3)
    print("===============")




def select_point(players,k):
    row1 = ["7" , "8" , "9"]
    row2 = ["4" , "5" , "6"]
    row3 = ["1" , "2" , "3"]
    X = []
    O = []
    while k == True:
        for i in players:
            choice = "10"
            board(row1,row2,row3)
            while k == True:
                choice = input(f"Your chance {i}")
                if choice is "poda": k = False
                if choice.isdigit()==True:
                    if int(choice) in range(1,10):
                        if choice not in X and choice not in O:
                            break       
            if i is "X":
                X.append(choice)
                if int(choice) in range(1,4):
                    choice = int(choice) - 1
                    row3[choice] = "X"
                    
                if int(choice) in range(4,7):
                    choice = int(choice) - 4
                    row2[choice] = "X"
                    
                if int(choice) in range(7,10):
                    choice = int(choice) - 7
                    row1[choice] = "X"
                
                if "1"in X and "2" in X and "3" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "4"in X and "5" in X and "6" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "7"in X and "8" in X and "9" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "1"in X and "4" in X and "7" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "8"in X and "2" in X and "5" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "9"in X and "6" in X and "3" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "1"in X and "5" in X and "9" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "7"in X and "5" in X and "3" in X:
                    print("Player 'X' has won the match")
                    k = False
                    board(row1,row2,row3)
                    
            elif i is "O":
                O.append(choice)
                if int(choice) in range(1,4):
                    choice = int(choice) - 1
                    row3[choice] = "O"
                    
                if int(choice) in range(4,7):
                    choice = int(choice) - 4
                    row2[choice] = "O"
                    
                if int(choice) in range(7,10):
                    choice = int(choice) - 7
                    row1[choice] = "O"
                    
                if "1"in X and "2" in O and "3" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "4"in O and "5" in O and "6" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "7"in O and "8" in O and "9" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "1"in O and "4" in O and "7" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "8"in O and "2" in O and "5" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "9"in O and "6" in O and "3" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "1"in O and "5" in O and "9" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)
                if "7"in O and "5" in O and "3" in O:
                    print("Player 'O' has won the match")
                    k = False
                    board(row1,row2,row3)





#uncomment lines below this and have fun!!!
k = True
select_point(user_select() , k)







