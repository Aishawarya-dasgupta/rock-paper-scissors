from tkinter import *
from PIL import Image,ImageTk
from random import randint 

window = Tk()
window.title("GAME")
window.configure(bg="black")


image_rock1 = ImageTk.PhotoImage(Image.open("rock-user.jpg"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper-user.jpg"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor-user.jpg"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock-comp.jpg"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper-comp.jpg"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor-comp.jpg"))

#insert pictures
label_computer = Label(window,image=image_scissor2,bg="black")
label_player = Label(window,image=image_scissor1,bg="black")
label_computer.grid(row=1 , column=0)
label_player.grid(row=1 , column=4)

#indicators
player_indicator = Label(window,font=50,text="USER",bg="black",fg="white")
comp_indicator = Label(window,font=50,text="COMPUTER",bg="black",fg="white")
player_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#buttons
rock = Button(window,width=16, height=3, text="ROCK", font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(window, width=16, height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(window,width=16, height=3 , text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

#scores
playerScore = Label(window,text=0,font=100,bg="black",fg="white")
computerScore =Label(window,text=0,font=100,bg="black",fg="white")
playerScore.grid(row=1,column=3)
computerScore.grid(row=1,column=1)

#messages
msg=Label(window,font=50,bg="black",fg="white")
msg.grid(row=3,column=2)

#Update Message
def updateMessage(x):
    msg['text'] = x

#update user Scores
def updatePlayerScores():
    score=int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

#update computer score
def updateComputerScores():
    score=int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("DRAW")
    elif player=="rock":
        if computer=="scissor":
            updateMessage("Player Wins")
            updatePlayerScores()
        else:
            updateMessage("Computer Wins")
            updateComputerScores()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("Computer Wins")
            updateComputerScores()
        else:
            updateMessage("Player Wins")
            updatePlayerScores()
    elif player=="scissor":
        if computer=="paper":
            updateMessage("Player Wins")
            updatePlayerScores()
        else:
            updateMessage("Computer Wins")
            updateComputerScores()
    else:
        pass


#update choices
choices=["rock","paper","scissor"]

def updateChoice(x):
    #for computer
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        label_computer.configure(image=image_rock2)
    elif compChoice=="paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    #for user
    if x=="rock":
        label_player.configure(image=image_rock1)
    elif x=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
        
    checkWin(x,compChoice)



 



window.mainloop()