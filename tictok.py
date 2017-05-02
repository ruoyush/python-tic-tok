player =0

def board():
    d={}
    for n in range(1,10):
        d[n]="-"
    return d
    
def printBoard(d):
    for k,v in d.items():
        if int(k)%3==0:
            print(k,v, end=" ")
            print("\n")
        else:
            print(k,v, end=" ")

def process(d):
    global player
    won =0
    if player == 0:
        x=int(input("Enter postion: "))
        y="O"
        d[x]=y
        player = 1
        won = check(d,x)
        if won ==1:
            print("tie")
        elif won ==2:
            print("Player1 won")
        elif won ==3:
            print("Player2 won")
        else:
            printBoard(d)
            process(d)


    else:
        x=int(input("Enter postion: "))
        y="X"
        d[x]=y
        player = 0
        won = check(d,x)
        if won ==1:
            print("tie")
        elif won ==2:
            print("Player1 won")
        elif won ==3:
            print("Player2 won")
        else:
            printBoard(d)
            process(d)


def check(d,n):
    contorl=0
    sumnum=0
    sv0=0
    sh0=0
    sd0=0
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

    for e in d.values():
        if e !="-":
            sumnum+=1
        
    if sumnum ==9:
        control = 1
        return control    
        
    

def main():
    d = board()
    printBoard(d)
    process(d)
    printBoard(d)
    x = input("Do you want to play again(y/n): ")
    if x =="y":
        main()
    else:
        pass

main()
