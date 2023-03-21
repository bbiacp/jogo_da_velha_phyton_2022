print ("Jogo da Velha 3x3")
import random

plays=0
players=2 
maxplays= 9
victory= "n"
playagain= "s"
game=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]]


def tela ():
    global jogo
    global plays
    print ("    0   1   2")
    print("0:  " +game[0][0]+" | "+ game[0][1]+" | "+ game[0][2])
    print("   ------------")
    print("1:  " +game[1][0]+" | "+ game[1][1]+" | "+ game[1][2])
    print("   ------------")
    print("2:  " +game[2][0]+" | "+ game[2][1]+" | "+ game[2][2])
    print("   ------------")
    print("Jogadas:"+ str(plays))

def playerplay():
    global plays
    global players
    global maxplays
    if players==2 and plays<maxplays:
        l=int(input("Line.:"))
        c=int(input("Spine.:"))
        try:
            while game[1][c]!= " ":
                l=int(input("Line..:"))
                s=int(input("Spine.:"))
            game[l][c]= "X"
            players=1
            plays+=1
        except:
            print ("Line e/ou Spine inexistente")
def automaticplay():
    global plays
    global players
    global maxplays
    if players==1 and plays<maxplays:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while game[1][c]!= " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        game[l][c]= "O"
        players=2
        plays+=1

def verificationvictory():
    global game
    victory="n"
    simbols= ["X","O"]
    for s in simbols:
        victory="n"
        il=0
        ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(game[il][ic]==s):
                    soma+=1
                ic+=1
            il+=1
            if(soma==3):
                victory = s
                break
        if (victory != "n"):
            break
        il=0
        ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(game[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                victory = s
                break
            ic+=1
        if (victory != "n"):
            break

        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if(game[idiagc][idiagl]==s):
                    soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            victory = s
            break
    return victory
def redifine ():
    global game
    global plays
    global players
    global maxplays
    global victory
    plays=0
    players=2
    maxplays= 9
    victory= "n"
    playagain= "s"
    game=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]] 
        
    
while (playagain=="s"):
    while True:
        tela()
        playerplay()
        automaticplay()
        tela()
        victory = verificationvictory()
        if(victory!="n")or (plays > maxplays):
            break
    print ("End Game")
    if(victory =="X" or victory=="O"):
        print("Você venceu " + victory)
    else:
        print ("Você empatou")
    playagain = input ("Você deseja jogar novamente? Digite s para sim e qualquer coisa para não:")
    redifine()
    
    
