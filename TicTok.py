'''
[]|[]\[]
[]\[]\[]
[]\[]\[]
'''

board = {"left top": " ", "middle top": " ", "right top": " ",
        "left middle": " ", "middle middle": " ", "right middle": " ",
        "left bottom": " ", "middle bottom": " ", "right bottom": " "}
lose = True
while lose:

    userinput = input("please enter X or O\n").upper()
    if (userinput != "X") and (userinput != "O"):
        print("Error you entered wrong character")
        break

    locationInput = input("please enter where\n").lower()
    if locationInput not in list(board.keys()):
        print("error you entered wrong location")
        break


    if board[locationInput] == "X" and "O":
        print("sorry u cant enter an already filled location")
        break



    board[locationInput] = userinput


    print(board["left top"] + "|" + board["middle top"] + "|" + board["right top"])
    print("– – –")
    print(board["left middle"] + "|" + board["middle middle"] + "|" + board["right middle"])
    print("– – –")
    print(board["left bottom"] + "|" + board["middle bottom"] + "|" + board["right bottom"])
# for X
    #rows
    if board["left top"] == "X"    and board["middle top"] == "X"    and board["right top"] == "X":
        lose = False
        print("you won")

    if board["left middle"] == "X" and board["middle middle"] == "X" and board["right middle"] == "X":
        lose = False
        print("you won")

    if board["left bottom"] == "X" and board["middle bottom"] == "X" and board["right bottom"] == "X":
        lose = False
        print("you won")
    #diagonally
    if board["left top"] == "X"    and board["middle middle"]== "X"   and board["right bottom"] == "X":
        lose = False
        print("you won")

    if board["left bottom"] == "X" and board["middle middle"]== "X"   and board["right top"] == "X":
        lose = False
        print("you won")
    #columns

    if board["left top"] == "X"    and board["left middle"] == "X"   and board["left bottom"] == "X":
        lose = False
        print("you won")

    if board["middle top"] == "X"  and board["middle middle"] == "X" and board["middle bottom"] == "X":
        lose = False
        print("you won")

    if board["right top"] == "X"   and board["right middle"] == "X" and board["right bottom"] == "X":
        lose = False
        print("you won")

# for O
    #rows
    if board["left top"] == "O"    and board["middle top"] == "O"    and board["right top"] == "O":
        lose = False
        print("you won")

    if board["left middle"] == "O" and board["middle middle"] == "O" and board["right middle"] == "O":
        lose = False
        print("you won")

    if board["left bottom"] == "O" and board["middle bottom"] == "O" and board["right bottom"] == "O":
        lose = False
        print("you won")
    #diagonally
    if board["left top"] == "O"    and board["middle middle"]== "O"   and board["right bottom"] == "O":
        lose = False
        print("you won")

    if board["left bottom"] == "O" and board["middle middle"]== "O"   and board["right top"] == "O":
        lose = False
        print("you won")
    #columns

    if board["left top"] == "O"    and board["left middle"] == "O"   and board["left bottom"] == "O":
        lose = False
        print("you won")

    if board["middle top"] == "O"  and board["middle middle"] == "O" and board["middle bottom"] == "O":
        lose = False
        print("you won")

    if board["right top"] == "O"   and board["right middle"] == "O" and board["right bottom"] == "O":
        lose = False
        print("you won")



