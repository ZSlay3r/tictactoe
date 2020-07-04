a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def turnOrder():
    while True:
        global currentTurn
        currentTurn = input("Who Will Go First: X or O?\nNote, The Best Way To Play Is If the Loser Of The Last Round Goes First - ")
        if currentTurn == "X" or currentTurn == "x":
            currentTurn = int(1)
            break
        elif currentTurn == "O" or currentTurn == "o":
            currentTurn = int(2)
            break
        print("\nError. Choose Either X or O To Go First\n")

def tttBoard():
    print(a[1] + "|" + a[2] + "|" + a[3])
    print("-+-+-")
    print(a[4] + "|" + a[5] + "|" + a[6])
    print("-+-+-")
    print(a[7] + "|" + a[8] + "|" + a[9])

def playerTurn():
    while True:
        pass
        global currentTurn
        if currentTurn%2 == 1:
            playerMarker = int(input("Player X, Choose A Spot - "))
        elif currentTurn%2 == 0:
            playerMarker = int(input("Player O, Choose A Spot - "))
        else:
            print("What how are you getting this message")

        if playerMarker > 0 and playerMarker <=9 and currentTurn%2 == 1:
            for i in range (len(a)):
                if a[i]== str(playerMarker):
                    a[i]= "X"
                    currentTurn = currentTurn + 1
            break
        elif playerMarker > 0 and playerMarker <=9 and currentTurn%2 == 0:
            for i in range (len(a)):
                if a[i]== str(playerMarker):
                    a[i]= "O"
                    currentTurn = currentTurn + 1
            break
        else:
            print("error")
            playerTurn()

    winCheck()

def winCheck():
    if (a[1] == a[2] and a[2] == a[3] and a[3] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[4] == a[5] and a[5] == a[6] and a[6] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[7] == a[8] and a[8] == a[9] and a[9] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[1] == a[4] and a[4] == a[7] and a[7] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[2] == a[5] and a[5] == a[8] and a[8] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[3] == a[6] and a[6] == a[9] and a[9] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[1] == a[5] and a[5] == a[9] and a[9] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    elif (a[2] == a[5] and a[5] == a[7] and a[7] == ("X" or "O")):
        print("\n" + a[1] + " Wins!")
    else:
        tttBoard()
        playerTurn()

turnOrder()
tttBoard()
playerTurn()
