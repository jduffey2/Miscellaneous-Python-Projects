# TextPad.py
# Author: Jason Duffey
# Date: 07/2015
# A textpad application for creating, editing, and saving files
import tkinter
from tkinter import filedialog
from tkinter import colorchooser
import ctypes
import sys

sel = ""
foreIndex = 0
backIndex = 0
def askSave():
	response = Mbox("Warning","Would you like to save?",3)
	if(7 == response):
		return True
	elif(6 == response):
		state = saveFile()
		if(state):
			return True
		else:
			return False
	else:
		return False

def Mbox(title, text, style):
	answer = ctypes.windll.user32.MessageBoxW(0,text,title,style)
	return answer

def showAbout():
	Mbox("About TextPad","You write on it and stuff.\n\n \tAuthor: Jason Duffey",0)

def showHelp():
	Mbox("Help","No Help Available",0)

def exitPad():
	response = askSave()
	if(response):
		sys.exit(0)
	else:
		return False

def newFile(*args):
	textArea.edit_separator()
	response = askSave()
	if(response):
		textArea.delete(1.0,"end-1c")
		textArea.edit_separator()
		return True
	else:
		return False

def openFile(*args):
	response = askSave()
	if(response):
		dialog = filedialog.askopenfilename(parent=top,title="Open",filetypes=(("All Files","*.*"),("Text Files","*.txt"),("Python","*.py"),("Documents","*.doc"),("Documents","*.docx")))
		if(dialog != ""):
			f = open(dialog,"r")
			doc = f.read()
			if(textArea.get(1.0,"end-1c") != ""):
				textArea.delete(1.0,"end-1c")
			textArea.insert(1.0,doc)
			textArea.edit_separator()
			f.close()
			return True
	return False

def saveFile(*args):
	textArea.edit_separator()
	dialog = filedialog.asksaveasfilename(defaultextension="txt",parent=top,title="Save",filetypes=(("All Files","*.*"),("Text Files","*.txt"),("Documents","*.doc"),("Documents","*.docx")))
	if(dialog != ""):
		f = open(dialog,"w")
		doc = textArea.get(1.0,"end-1c")
		f.write(doc)
		f.close()
		return True
	return False

def cutText(*args):
	textArea.edit_separator()
	copyText()
	textArea.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
	textArea.edit_separator()

def copyText(*args):
	global sel
	sel = textArea.selection_get()

def pasteText(*args):
	global sel
	textArea.edit_separator()
	position = textArea.index(tkinter.INSERT)
	textArea.insert(position,sel)
	textArea.edit_separator()

def changeColor(*args):
	global foreIndex
	tag = "color" + str(foreIndex)
	foreIndex += 1
	textArea.tag_add(tag,tkinter.SEL_FIRST,tkinter.SEL_LAST)
	newColor = colorchooser.askcolor(color="White",title="Color Chooser")
	textArea.tag_config(tag,foreground=newColor[1])

def changeBackColor(*args):
	global backIndex
	tag = "back" + str(backIndex)
	backIndex += 1
	textArea.tag_add(tag,tkinter.SEL_FIRST,tkinter.SEL_LAST)
	newColor = colorchooser.askcolor(color="White",title="Color Chooser")
	textArea.tag_config(tag,background=newColor[1])

def undoText(*args):
	try:
		textArea.edit_undo()
	except:
		pass

def redoText(*args):
	try:
		textArea.edit_redo()
	except:
		pass

def addSeparator(*args):
	textArea.edit_separator()

# Create GUI
#----------------------------------------------------------
#----------------------------------------------------------

top = tkinter.Tk()
top.wm_title("TextPad")
top.protocol("WM_DELETE_WINDOW",exitPad)

# Menu Configuration
#----------------------------------------------------------
menubar = tkinter.Menu(top)

#add the File menu and its subitems
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exitPad)
menubar.add_cascade(label="File", menu=filemenu)

#add the Edit menu and its subitems
editmenu = tkinter.Menu(menubar)
editmenu.add_command(label="Cut",command=cutText)
editmenu.add_command(label="Copy",command=copyText)
editmenu.add_command(label="Paste",command=pasteText)
editmenu.add_separator()
editmenu.add_command(label="Undo",command=undoText)
editmenu.add_command(label="Redo",command=redoText)
editmenu.add_separator()
editmenu.add_command(label="Font Color...",command=changeColor)
editmenu.add_command(label="Background Color...",command=changeBackColor)
menubar.add_cascade(label="Edit",menu=editmenu)

#add the Help menu and its subitems
helpmenu = tkinter.Menu(menubar)
helpmenu.add_command(label="About",command=showAbout)
helpmenu.add_separator()
helpmenu.add_command(label="Help",command=showHelp)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)
#----------------------------------------------------------

#Configure the textArea and it's shortcuts
textArea = tkinter.Text(top,width="120",height="50",undo=True)
textArea.edit_separator()
textArea.bind("<Control-x>",cutText)
textArea.bind("<Control-c>",copyText)
textArea.bind("<Control-v>",pasteText)
textArea.bind("<Control-o>",openFile)
textArea.bind("<Control-s>",saveFile)
textArea.bind("<Control-n>",newFile)
textArea.bind("<Control-z>",undoText)
textArea.bind("<Control-y>",redoText)
textArea.bind("<Control-\>",addSeparator)
textArea.pack(fill=tkinter.BOTH,expand=1)

top.mainloop()