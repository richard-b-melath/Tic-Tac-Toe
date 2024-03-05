#PLAYER NAME
player1 = input("Enter player 1 name : ")
player2 = input("Enter player 2 name : ")

#GENERAL RULES

#GENERAL VARIABLES
board = {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1, 7:-1, 8:-1, 9:-1}
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
count = 0
chance = 0
completed = 0
check = 0

#ANALYZING THE BOARD
def analyze():
    for j in range(0,8):
        if(board[win[j][0]]==0 and board[win[j][0]]==board[win[j][1]] and board[win[j][0]]==board[win[j][2]]):
            return 7
        elif(board[win[j][0]]==1 and board[win[j][0]]==board[win[j][1]] and board[win[j][0]]==board[win[j][2]]):
            return 10

#GAME BOARD
def Board():
    print("-------------")
    for i in range (1,10):
        if i%3==1:
            print("|",end=" ")
        if(board[i]==-1):
            print(" ",end=" | ")
        if(board[i]==0):
            print("X",end=" | ")
        if(board[i]==1):
            print("O",end=" | ")
        if i%3==0:
            print(" ")
            print("-------------")
    




#GAME PLAY
def player(move):
    if board[move]!=-1:
        return -1
    else:
        if(chance==0):
            board[move]=0
        else:
            board[move]=1


while(count!=9):
    Board()
    check = analyze()
    if(check==7 or check==10):
        break
    if(chance==0):
        print(player1,end=" : ")
    else:
        print(player2,end=" : ")
    move = int(input())
    completed = player(move)
    if(completed==-1):
        print("Error move Replay!!!")
        continue
    else:
        chance = (chance+1)%2
        count = count + 1

Board()
if(check==7):
        print(player1," WINS!!!!!")
elif(check==10):
        print(player2," WINS!!!!!")
else:
        print("!!!||||Its a DRAW||||!!!")

ex = input("Enter any switch to exit")