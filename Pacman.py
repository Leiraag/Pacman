from tkinter import *
from tkinter import messagebox
from random import *
import time

murs = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,5,3,3,5,3,3,3,5,1,5,3,3,3,5,3,3,5,1],
        [1,4,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,4,1],
        [1,5,3,3,5,3,5,3,5,3,5,3,5,3,5,3,3,5,1],
        [1,3,1,1,3,1,3,1,1,1,1,1,3,1,3,1,1,3,1],
        [1,5,3,3,5,1,5,3,5,1,5,3,5,1,5,3,3,5,1],
        [1,1,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,1,1],
        [1,1,1,1,3,1,5,3,5,5,5,3,5,1,3,1,1,1,1],
        [1,1,1,1,3,1,3,1,1,2,1,1,3,1,3,1,1,1,1],
        [1,1,1,1,5,3,5,1,2,2,2,1,5,3,5,1,1,1,1],
        [1,1,1,1,3,1,3,1,1,1,1,1,3,1,3,1,1,1,1],
        [1,1,1,1,3,1,5,3,3,3,3,3,5,1,3,1,1,1,1],
        [1,1,1,1,3,1,3,1,1,1,1,1,3,1,3,1,1,1,1],
        [1,5,3,3,5,3,5,3,5,1,5,3,5,3,5,3,3,5,1],
        [1,3,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,3,1],
        [1,6,5,1,5,3,5,3,5,0,5,3,5,3,5,1,5,6,1],
        [1,1,3,1,3,1,3,1,1,1,1,1,3,1,3,1,3,1,1],
        [1,5,5,3,5,1,5,3,5,1,5,3,5,1,5,3,5,5,1],
        [1,3,1,1,1,1,1,1,3,1,3,1,1,1,1,1,1,3,1],
        [1,5,3,3,3,3,3,3,5,3,5,3,3,3,3,3,3,5,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


invincible = 0
tinvincible = 0
score = 0
Fspeed = 200
def victoire():
    if score == 172:
        messagebox.showinfo("Game", "YOU Win")
        fen.destroy()

def invincibilite():
    global tinvincible
    global invincible
    invincible = 1
    if tinvincible == 100:
        invincible = 0
        print("attention")
    else:
        tinvincible +=1
        fen.after(100, invincibilite)

def FRedMouvement():
    global FRedDirection
    global Fspeed
    FRedmur=1
    FRedx1,FRedy1,FRedx2,FRedy2 = zone.coords(FRed)
    FRedx= int(FRedx1//25)
    FRedy= int(FRedy1//25)
    while FRedmur == 1:
        if murs[FRedy][FRedx] == 5:
            FRedDirection =randrange(1,5)
        if murs[FRedy][FRedx] == 6:
            FRedDirection =randrange(1,5)
        if murs[FRedy][FRedx] == 2:
            FRedDirection =randrange(1,5)


        if FRedDirection == 1:
            if FRedx1 == 425:
                zone.coords(FRed,25,225,50,250)
            elif murs[FRedy][FRedx+1] == 1:
                FRedmur=1
            else:
                FRedmur=0
                zone.coords(FRed,FRedx1+25,FRedy1,FRedx2+25,FRedy2)
                #print("droite")

        elif FRedDirection == 2:
            if FRedx1 == 0:
                    zone.coords(FRed,450,225,475,250)
            elif murs[FRedy][FRedx-1] == 1:
                FRedmur=1
            else:
                FRedmur=0
                zone.coords(FRed,FRedx1-25,FRedy1,FRedx2-25,FRedy2)
                #print("gauche")

        elif FRedDirection == 3:
            if murs[FRedy-1][FRedx] == 1:
                FRedmur=1
            else:
                FRedmur=0
                zone.coords(FRed,FRedx1,FRedy1-25,FRedx2,FRedy2-25)
                #print("haut")

        elif FRedDirection == 4:
            if murs[FRedy+1][FRedx] == 1:
                FRedmur=1
            else:
                FRedmur=0
                zone.coords(FRed,FRedx1,FRedy1+25,FRedx2,FRedy2+25)
                #print("bas")

        Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
        FRedx1,FRedy1,FRedx2,FRedy2 = zone.coords(FRed)
        if FRedx1 == Pacmanx1:
            if FRedy1 == Pacmany1:
                if invincible == 0:
                    messagebox.showinfo("Game", "YOU LOSE")
                    fen.destroy()
                else:
                    zone.coords(FRed,225,225,250,250)



    fen.after(Fspeed, FRedMouvement)


def FPinkMouvement():
    global FPinkDirection
    global Fspeed
    FPinkmur=1
    FPinkx1,FPinky1,FPinkx2,FPinky2 = zone.coords(FPink)
    FPinkx= int(FPinkx1//25)
    FPinky= int(FPinky1//25)
    while FPinkmur == 1:
        if murs[FPinky][FPinkx] == 5:
            FPinkDirection =randrange(1,5)
        if murs[FPinky][FPinkx] == 6:
            FPinkDirection =randrange(1,5)
        if murs[FPinky][FPinkx] == 2:
            FPinkDirection =randrange(1,5)

        if FPinkDirection == 1:
            if FPinkx1 == 425:
                zone.coords(FPink,25,225,50,250)
            elif murs[FPinky][FPinkx+1] == 1:
                FPinkmur=1
            else:
                FPinkmur=0
                zone.coords(FPink,FPinkx1+25,FPinky1,FPinkx2+25,FPinky2)
                #print("droite")

        elif FPinkDirection == 2:
            if FPinkx1 == 0:
                zone.coords(FPink,450,225,475,250)
            elif murs[FPinky][FPinkx-1] == 1:
                FPinkmur=1
            else:
                FPinkmur=0
                zone.coords(FPink,FPinkx1-25,FPinky1,FPinkx2-25,FPinky2)
                #print("gauche")

        elif FPinkDirection == 3:
            if murs[FPinky-1][FPinkx] == 1:
                FPinkmur=1
            else:
                FPinkmur=0
                zone.coords(FPink,FPinkx1,FPinky1-25,FPinkx2,FPinky2-25)
                #print("haut")

        elif FPinkDirection == 4:
            if murs[FPinky+1][FPinkx] == 1:
                FPinkmur=1
            else:
                FPinkmur=0
                zone.coords(FPink,FPinkx1,FPinky1+25,FPinkx2,FPinky2+25)
                #print("bas")

        Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
        FPinkx1,FPinky1,FPinkx2,FPinky2 = zone.coords(FPink)
        if FPinkx1 == Pacmanx1:
            if FPinky1 == Pacmany1:
                if invincible == 0:
                    messagebox.showinfo("Game", "YOU LOSE")
                    fen.destroy()
                else:
                    zone.coords(FPink,225,225,250,250)
    fen.after(Fspeed, FPinkMouvement)


def FBlueMouvement():
    global FBlueDirection
    global Fspeed
    FBluemur=1
    FBluex1,FBluey1,FBluex2,FBluey2 = zone.coords(FBlue)
    FBluex= int(FBluex1//25)
    FBluey= int(FBluey1//25)
    while FBluemur == 1:
        if murs[FBluey][FBluex] == 5:
            FBlueDirection =randrange(1,5)
        if murs[FBluey][FBluex] == 6:
            FBlueDirection =randrange(1,5)
        if murs[FBluey][FBluex] == 2:
            FBlueDirection =randrange(1,5)

        if FBlueDirection == 1:
            if FBluex1 == 425:
                zone.coords(FBlue,25,225,50,250)
            elif murs[FBluey][FBluex+1] == 1:
                FBluemur=1
            else:
                FBluemur=0
                zone.coords(FBlue,FBluex1+25,FBluey1,FBluex2+25,FBluey2)
                #print("droite")

        elif FBlueDirection == 2:
            if FBluex1 == 0:
                zone.coords(FBlue,450,225,475,250)
            if murs[FBluey][FBluex-1] == 1:
                FBluemur=1
            else:
                FBluemur=0
                zone.coords(FBlue,FBluex1-25,FBluey1,FBluex2-25,FBluey2)
                #print("gauche")

        elif FBlueDirection == 3:
            if murs[FBluey-1][FBluex] == 1:
                FBluemur=1
            else:
                FBluemur=0
                zone.coords(FBlue,FBluex1,FBluey1-25,FBluex2,FBluey2-25)
                #print("haut")

        elif FBlueDirection == 4:
            if murs[FBluey+1][FBluex] == 1:
                FBluemur=1
            else:
                FBluemur=0
                zone.coords(FBlue,FBluex1,FBluey1+25,FBluex2,FBluey2+25)
                #print("bas")

        Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
        FBlueFx1,FBluey1,FNluex2,FBluey2 = zone.coords(FBlue)
        if FBluex1 == Pacmanx1:
            if FBluey1 == Pacmany1:
                if invincible == 0:
                    messagebox.showinfo("Game", "YOU LOSE")
                    fen.destroy()
                else:
                    zone.coords(FBlue,225,225,250,250)
    fen.after(Fspeed, FBlueMouvement)


def FOrangeMouvement():
    global FOrangeDirection
    global Fspeed
    FOrangemur=1
    FOrangex1,FOrangey1,FOrangex2,FOrangey2 = zone.coords(FOrange)
    FOrangex= int(FOrangex1//25)
    FOrangey= int(FOrangey1//25)
    while FOrangemur == 1:
        if murs[FOrangey][FOrangex] == 5:
            FOrangeDirection =randrange(1,5)
        if murs[FOrangey][FOrangex] == 6:
            FOrangeDirection =randrange(1,5)
        if murs[FOrangey][FOrangex] == 2:
            FOrangeDirection =randrange(1,5)

        if FOrangeDirection == 1:
            if FOrangex1 == 425 :
                zone.coords(FOrange,25,225,50,250)

            elif murs[FOrangey][FOrangex+1] == 1:
                FOrangemur=1
            else:
                FOrangemur=0
                zone.coords(FOrange,FOrangex1+25,FOrangey1,FOrangex2+25,FOrangey2)
                #print("droite")

        elif FOrangeDirection == 2:
            if FOrangex1 == 0:
                zone.coords(FOrange,450,225,475,250)
            elif murs[FOrangey][FOrangex-1] == 1:
                FOrangemur=1
            else:
                FOrangemur=0
                zone.coords(FOrange,FOrangex1-25,FOrangey1,FOrangex2-25,FOrangey2)
                #print("gauche")

        elif FOrangeDirection == 3:
            if murs[FOrangey-1][FOrangex] == 1:
                FOrangemur=1
            else:
                FOrangemur=0
                zone.coords(FOrange,FOrangex1,FOrangey1-25,FOrangex2,FOrangey2-25)
                #print("haut")

        elif FOrangeDirection == 4:
            if murs[FOrangey+1][FOrangex] == 1:
                FOrangemur=1
            else:
                FOrangemur=0
                zone.coords(FOrange,FOrangex1,FOrangey1+25,FOrangex2,FOrangey2+25)
                #print("bas")

        Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
        FOrangex1,FOrangey1,FOrangex2,FOrangey2 = zone.coords(FOrange)
        if FOrangex1 == Pacmanx1:
            if FOrangey1 == Pacmany1:
                if invincible == 0:
                    messagebox.showinfo("Game", "YOU LOSE")
                    fen.destroy()
                else:
                    zone.coords(FOrange,225,225,250,250)

    fen.after(Fspeed, FOrangeMouvement)










def PacmanDeplaceD(event):
    global score
    global tinvincible
    Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman) #on récupère les coordonnées du perso
    Pacmanx=int(Pacmanx1//25+1)
    Pacmany=int(Pacmany1//25)
    if Pacmanx1 == 450:
        zone.coords(Pacman,0,225,25,250)
    elif murs[Pacmany][Pacmanx] == 1 :
        pass
    elif murs[Pacmany][Pacmanx] == 2:
        pass
    else:
        item = zone.find_closest(Pacmanx1+40, Pacmany1+15)[0]
        print(zone.gettags(item))
        if "Pacgomme" in zone.itemconfig(item)["tags"]:
            zone.delete(item)
            score += 1
            victoire()
            print(score)
        elif "SuperPacgomme" in zone.itemconfig(item)["tags"]:
            tinvincible =0
            zone.delete(item)
            invincibilite()
        zone.coords(Pacman,Pacmanx*25,Pacmany*25,Pacmanx*25+25,Pacmany*25+25)



def PacmanDeplaceG(event):
    global score
    global tinvincible
    Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
    Pacmanx=int(Pacmanx1//25-1)
    Pacmany=int(Pacmany1//25)
    if Pacmanx1 == 0:
        zone.coords(Pacman,450,225,475,250)
    elif murs[Pacmany][Pacmanx] == 1 :
        pass
    elif murs[Pacmany][Pacmanx] == 2:
        pass
    else:
        item = zone.find_closest(Pacmanx1-15, Pacmany1+15)[0]
        print(zone.gettags(item))
        if "Pacgomme" in zone.itemconfig(item)["tags"]:
            zone.delete(item)
            score += 1
            victoire()
            print(score)
        elif "SuperPacgomme" in zone.itemconfig(item)["tags"]:
            tinvincible =0
            invincibilite()
            zone.delete(item)
        zone.coords(Pacman,(Pacmanx*25)%475,Pacmany*25,(Pacmanx*25+25)%475,Pacmany*25+25)


def PacmanDeplaceH(event):
    global score
    global tinvincible
    Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
    Pacmanx=int(Pacmanx1//25)
    Pacmany=int(Pacmany1//25-1)
    if murs[Pacmany][Pacmanx] == 1 :
        pass
    elif murs[Pacmany][Pacmanx] == 2:
        pass
    else:
        item = zone.find_closest(Pacmanx1+15, Pacmany1+-15)[0]
        print(zone.gettags(item))
        if "Pacgomme" in zone.itemconfig(item)["tags"]:
            zone.delete(item)
            score += 1
            victoire()
            print(score)
        elif "SuperPacgomme" in zone.itemconfig(item)["tags"]:
            tinvincible =0
            zone.delete(item)
            invincibilite()
        zone.coords(Pacman,Pacmanx1,Pacmany1-25,Pacmanx2,Pacmany2-25)


def PacmanDeplaceB(event):
    global score
    global tinvincible
    Pacmanx1,Pacmany1,Pacmanx2,Pacmany2 = zone.coords(Pacman)
    Pacmanx=int(Pacmanx1//25)
    Pacmany=int(Pacmany1//25+1)
    if murs[Pacmany][Pacmanx] == 1 :
        pass
    elif murs[Pacmany][Pacmanx] == 2:
        pass
    else:
        item = zone.find_closest(Pacmanx1+15, Pacmany1+40)[0]
        print(zone.gettags(item))
        if "Pacgomme" in zone.itemconfig(item)["tags"]:
            zone.delete(item)
            score += 1
            victoire()
            print(score)
        elif "SuperPacgomme" in zone.itemconfig(item)["tags"]:
            tinvincible =0
            invincibilite()
            zone.delete(item)
        zone.coords(Pacman,Pacmanx1,Pacmany1+25,Pacmanx2,Pacmany2+25)

#Fantome Rouge




#fenetre
fen = Tk()

zone = Canvas(fen,height = 525, width=475,bg="ivory")
zone.grid()

Pacman = zone.create_oval(225,375,250,400,fill = "yellow",outline = "red",tags='perso') #creation de notre personnage
FRed = zone.create_oval(225,200,250,225,fill = "red",outline = "red")
FPink = zone.create_oval(225,225,250,250,fill = "pink",outline = "pink")
FBlue = zone.create_oval(200,225,225,250,fill = "blue",outline = "blue")
FOrange = zone.create_oval(250,225,275,250,fill = "orange",outline = "orange")


#FRed = zone.create_polygon(0,50,12,25,25,50,fill = "red",outline = "red") #creation de notre personnage

#grille
for i in range(19):
    zone.create_line(25*i,0,25*i,525,fill='black')
for i in range(21):
    zone.create_line(0,25*i,475,25*i,fill='black')

#mur
for murY in range(21):
    for murX in range(19):
        if murs[1*murY][1*murX] == 1:
            zone.create_rectangle(25*murX,25*murY,25*murX+25,25*murY+25,fill="black")

#Pacgomme
for murY in range(21):
    for murX in range(19):
        if murs[1*murY][1*murX] == 3 :
            zone.create_oval(25*murX+10,25*murY+10,25*murX+15,25*murY+15,fill="yellow",tags="Pacgomme")
        elif murs[1*murY][1*murX] == 5 :
            zone.create_oval(25*murX+10,25*murY+10,25*murX+15,25*murY+15,fill="yellow",tags="Pacgomme")

#SuperPacgomme
for murY in range(21):
    for murX in range(19):
        if murs[1*murY][1*murX] == 4 :
            zone.create_oval(25*murX+5,25*murY+5,25*murX+20,25*murY+20,fill="cyan",tags="SuperPacgomme")
        elif murs[1*murY][1*murX] == 6 :
            zone.create_oval(25*murX+5,25*murY+5,25*murX+20,25*murY+20,fill="cyan",tags="SuperPacgomme")



#tracer()


zone.bind_all('<Right>', PacmanDeplaceD)
zone.bind_all('<Left>', PacmanDeplaceG)
zone.bind_all('<Up>', PacmanDeplaceH)
zone.bind_all('<Down>', PacmanDeplaceB)
FRedMouvement()
FPinkMouvement()
FBlueMouvement()
FOrangeMouvement()


fen.mainloop()