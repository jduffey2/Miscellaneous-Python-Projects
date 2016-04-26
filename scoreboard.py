# scoreboard.py
# Author: Jason Duffey
# Date: 01/2016
# A simple scoreboard, Ctrl adds to the respective scores
# Space resets the score
import tkinter

player1 = 0
player2 = 0
# player1Score = tkinter.StringVar()
# player2Score = tkinter.StringVar()
# player1Score.set(str(player1))
# player2Score.set(str(player2))

top = tkinter.Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
top.geometry(str(width) + "x" + str(height))
top.wm_title("Scoreboard")

score1 = tkinter.Label(top,text=player1,width=100,font=("Helvetica",int(height/2)),fg="red")
score2 = tkinter.Label(top,text=player2,width=100,font=("Helvetica",int(height/2)),fg="blue")
score1.place(x=0,y=0,width=int(width/2),height=height)
score2.place(x=int(width/2),y=0,width=int(width/2),height=height)

def player1Score(event):
	global player1
	player1 += 1
	score1.config(text=str(player1))

def player2Score(event):
	global player2
	player2 += 1
	score2.config(text=str(player2))

def reset(event):
	global player1, player2
	player1 = player2 = 0
	score2.config(text=str(player2))
	score1.config(text=str(player1))

top.bind("<Control_L>", player1Score)
top.bind("<Control_R>", player2Score)
top.bind("<space>", reset)

top.focus_set()
top.mainloop()