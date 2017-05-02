def board():
    print("Welcome to the tic tok toe game. Player 1 will use 'O' as mark. Player 2 will use 'X' as mark.")
    d={}
    for n in range(1,10):
        d[n]="-"
    return d
    
def printBoard(d):
    for k,v in d.items():
        if int(k)%3==0:
            print(v, end=" ")
            print("\n")
        else:
            print(v, end=" ")

def checkInput(d): # take input and check if the input is valid
    
    x=""
    # try: # check if the input is a number
    #     x=int(x)
    # except ValueError:
    #     print("Enter number please")
    #     continue
    
    while x not in '1 2 3 4 5 6 7 8 9'.split() or not checkSingle(d,int(x)):  # check if the number is in the range of 1 to 9
            x=input("Please enter correct number(only number from 1-9): ")
    
    return int(x)

def checkSingle(d,x): # check if the space has been filled
    return d[x] == "-"

def checkWon(d,n):
    contorl=0 # 0 for ongoing, 1 for tie, 2 for player1 won, 3 for player3 won
    sumnum=0 # tie counter
    sv0=0 # player1 vertical counter
    sh0=0 # player1 horizonal counter
    sd0=0 # player1 dignose counter
    sv1=0
    sh1=0 
    sd1=0
            
    if n >3 and n<7:
        for e in [n-3,n+3]:
            if d[e] == "O":
                sv0 +=1
            elif d[e] == "X":
                sv1 +=1
            else:
                pass
        for e in [4,5,6]:
            if d[e]=="O":
                sh0 +=1
            elif d[e] == "X":
                sh1 +=1
            else:
                pass
        if sh0==3 or sv0==3:
            control = 2
            return control
        if sh1==3 or sv1==3:
            control = 3
            return control
    elif n<4:
        for e in [n+3,n+6]:
            if d[e] == "O":
                sv0 +=1
            elif d[e] == "X":
                sv1 +=1
            else:
                pass
        for e in [1,2,3]:
            if d[e]=="O":
                sh0 +=1
            elif d[e] == "X":
                sh1 +=1
            else:
                pass
        if n==1:
            for e in [1,5,9]:
                if d[e]=="O":
                    sd0+=1
                elif d[e] =="X":
                    sd1+=1
                else:
                    pass
        if n==3:
            for e in [3,5,7]:
                if d[e]=="O":
                    sd0+=1
                elif d[e] =="X":
                    sd1+=1
                else:
                    pass            
        if sh0==3 or sv0==3 or sd0==3:
            control = 2
            return control
        if sh1==3 or sv1==3 or sd1==3:
            control = 3
            return control
    elif n>6:
        for e in [n-3,n-6]:
            if d[e] == "O":
                sv0 +=1
            elif d[e] == "X":
                sv1 +=1
            else:
                pass
        for e in [7,8,9]:
            if d[e]=="O":
                sh0 +=1
            elif d[e] == "X":
                sh1 +=1
            else:
                pass
        if n==7:
            for e in [3,5,7]:
                if d[e]=="O":
                    sd0+=1
                elif d[e] =="X":
                    sd1+=1
                else:
                    pass
        if n==9:
            for e in [1,5,9]:
                if d[e]=="O":
                    sd0+=1
                elif d[e] =="X":
                    sd1+=1
                else:
                    pass    
        if sh0==3 or sv0==3 or sd0==3:
            control = 2
            return control
        if sh1==3 or sv1==3 or sd1==3:
            control = 3
            return control   
    else:
        pass

    # for e in d.values():
    #     if e !="-":
    #         sumnum+=1
        
    if "-" not in d.values():
        control =1
        
    # if sumnum ==9:
    #     control = 1
        
        return control    
    
def process(d,player):
    won =0
    
    x=checkInput(d)
    print("Player",(player+1),"selected position",x) 
    if player == 0:
        d[x]="O"
        player = 1
        won = checkWon(d,x)
        if won ==1:
            print("tie")
        elif won ==2:
            print("Player1 won")
        elif won ==3:
            print("Player2 won")
        else:
            printBoard(d)
            process(d,player)

    else:
        d[x]="X"
        player = 0
        won = checkWon(d,x)
        if won ==1:
            print("tie")
        elif won ==2:
            print("Player1 won")
        elif won ==3:
            print("Player2 won")
        else:
            printBoard(d)
            process(d,player)



def replay():
    x = input("Do you want to play again(y/n): ").lower().startswith("y")
    if  x == True:
        player =0
        main()
    else:
        print("Bye!")
        pass

def main():
    player = 0 # set the player switch 
    
    d = board() # init the board
    
    printBoard(d) # print the blank board
    
    process(d,player) # game on
    
    printBoard(d) # print the final board
    
    replay() # ask if the players wnat to play next round


main()
