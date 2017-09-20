a1=  'p1'
a2 = 'p2'
a3 = 'p3'
a4 = 'p4'
a5 = 'p5'
a6 = 'p6'
a7 = 'p7'
a8 = 'p8'
a9 = 'p9'
choices=[a1,a2,a3,a4,a5,a6,a7,a8,a9]

def play():
    global choices
    x1=[]
    x2=[]

    print(choices[0]+'\t'+choices[1]+'\t'+choices[2]+'\n'+choices[3]+'\t'+choices[4]+'\t'+choices[5]+'\n'+choices[6]+'\t'+choices[7]+'\t'+choices[8]+'\n')
    s7=[a1,a5,a9]
    s8=[a3,a5,a7]
    s1 = [a1, a2, a3]
    s2 = [a4, a5, a6]
    s3 = [a7, a8, a9]
    s4 = [a1, a4, a7]
    s5 = [a2, a5, a8]
    s6 = [a3, a6, a9]
    sol=[s1,s2,s3,s4,s5,s6,s7,s8]
    n=1
    while(n<=9):
        if(n%2!=0):
            x1=player1(x1)
            if(len(x1)==3):
                for p in sol:
                    if(x1==p):
                        print("Congrats player one has won the game")
                        return
                    else:
                        break
            n+=1
        else:
            x2=player2(x2)
            if (len(x1) == 3):
                for p in sol:
                    if (x1 == p):
                        print("Congrats player one has won the game")
                        return
                    else:
                        break
            n+=1
    print("Sorry the game has ended in a draw")
    x=raw_input("Press P to start a new game")
    if(x.lower()=='p'):
        play()
    else:
        exit
def player1(x1):
    global choices
    i1=raw_input("PLayer 1 Enter your choice amongst available...")
    x1.append(i1)
    n=choices.index(i1)
    choices[n]='x1'
    print(choices[0] + '\t' + choices[1] + '\t' + choices[2] + '\n' + choices[3] + '\t' + choices[4] + '\t' + choices[5] + '\n' + choices[6] + '\t' + choices[7] + '\t' + choices[8] + '\n')
    return x1

def player2(x2):
    global choices
    i2=raw_input("PLayer 2 Enter your choice amongst available...")
    x2.append(i2)
    n = choices.index(i2)
    choices[n] = 'x2'
    print(choices[0] + '\t' + choices[1] + '\t' + choices[2] + '\n' + choices[3] + '\t' + choices[4] + '\t' + choices[5] + '\n' + choices[6] + '\t' + choices[7] + '\t' + choices[8] + '\n')
    return x2

play()
