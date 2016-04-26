# Simon.py
# Author: Jason Duffey
# Date: 07/2015
# An implementation of the game of Simon
# keeps track of the high score of the games
import time
import tkinter
import random
from atexit import register
delay = 500
current_guess = 0
seq = []
length = 3
score = 0
can_guess = False
wrong = 0
highScore = 0

def restart():
    global delay, current_guess,length,score,can_guess,wrong
    delay = 500
    current_guess = 0
    length = 3
    score = 0
    can_guess = False
    wrong = 0
    scoreLbl.config(text=str(score))
    wrongLbl.config(text="")

def blink(rec,color,canvas):
    global delay
    current = canvas.itemcget(rec,"fill")
    canvas.itemconfigure(rec,fill=color)
    if(color == "pink" or color == "lightblue" or color == "lightyellow" or color == "lightgreen"):
        canvas.after(delay,blink,rec,current,canvas)

def activate():
    global can_guess
    can_guess = True

def addrec():
    global bluerec, can, redrec, greenrec, yellowrec, delay,length,seq,current_guess,can_guess
    seq = []
    dela = 2*delay
    current_guess = 0
    can_guess = False
    for x in range(1,1+length):
        seq.append(random.randint(0,3))
    
    for color in range(0,length):
        if seq[color] == 0:
            can.after(dela * color,blink,bluerec,"lightblue",can)
        elif seq[color] == 1:
            can.after(dela * color,blink,redrec,"pink",can)
        elif seq[color] == 2:
            can.after(dela * color,blink,yellowrec,"lightyellow",can)
        else:
            can.after(dela * color,blink,greenrec,"lightgreen",can)
    can.after(dela * length,lambda: activate())
    length = length + 1
    if delay > 200:
        delay = delay - 30

def checkSequence(guess):
    global seq,current_guess, score, can_guess, scoreLbl, wrong, can, highScore
    if can_guess: 
        if current_guess >= length - 1:
            print("SEQUENCE CORRECT")
            return
        if(seq[current_guess] != guess):
            wrong = wrong + 1
            text = ""
            for strike in range(0,wrong):
                text = text + "X"
            wrongLbl.config(text=text)
            if(wrong == 3):
                restart()
        else:
            score = score + 25
            if(current_guess >= length - 2):
                score = score + 100
                can_guess = False
            scoreLbl.config(text=str(score))
            if(score > highScore):
                highScore = score
                hiScoreLbl.config(text=str(score))
            current_guess = current_guess + 1

def getHighScore():
    global highScore
    f = open("simonHighScore.txt","r")
    scr = f.read()
    hiScoreLbl.config(text=str(scr))
    highScore = int(scr)
    f.close()

def saveHighScore():
    global highScore
    f = open("simonHighScore.txt","w")
    f.write(str(highScore))
    f.close()



top = tkinter.Tk()
top.wm_title("Simon")
slbl = tkinter.Label(top,text="Score: ")
slbl.pack()
scoreLbl = tkinter.Label(top,text="0")
scoreLbl.pack()
wrongLbl = tkinter.Label(top)
wrongLbl.place(x="300",y="0")
hslbl = tkinter.Label(top,text="High Score: ")
hslbl.place(x="0",y="0")
hiScoreLbl = tkinter.Label(top,text="0")
hiScoreLbl.place(x="80",y="0")
can = tkinter.Canvas(top,width="400",height="400",bg="white")
can.pack()
bluerec = can.create_rectangle(0,0,200,200,fill="blue")
redrec = can.create_rectangle(200,0,400,200,fill="red")
yellowrec = can.create_rectangle(0,200,200,400,fill="yellow")
greenrec = can.create_rectangle(200,200,400,400,fill="green")
can.tag_bind(bluerec,"<Button-1>",lambda event:checkSequence(0))
can.tag_bind(redrec,"<Button-1>",lambda event:checkSequence(1))
can.tag_bind(yellowrec,"<Button-1>",lambda event:checkSequence(2))
can.tag_bind(greenrec,"<Button-1>",lambda event:checkSequence(3))
btn = tkinter.Button(top,text="Show",command=addrec)
btn.pack()
getHighScore()
register(saveHighScore)
top.mainloop()