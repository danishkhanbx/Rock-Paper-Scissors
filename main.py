from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main Window
root = Tk()
root.title('Rock-Paper-Scissors')
root.minsize(860, 300)
root.maxsize(860, 300)
root.configure(background='#9b59b6')

# Pictures
rock_img = ImageTk.PhotoImage(Image.open('rock-user.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper-user.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissors-user.png'))
rock_img_comp = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img_comp = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img_comp = ImageTk.PhotoImage(Image.open('scissors.png'))

# Insert Pictures
user_label = Label(root, image=scissor_img, bg='#9b59b6')
comp_label = Label(root, image=scissor_img_comp, bg='#9b59b6')
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
playerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=50, text='USER', bg='#9b59b6', fg='white')
comp_indicator = Label(root, font=50, text='COMPUTER', bg='#9b59b6', fg='white')
comp_indicator.grid(row=0, column=1)
user_indicator.grid(row=0, column=3)

# Messages
msg = Label(root, font=50, bg='#9b59b6', fg='white')
msg.grid(row=3, column=2)


# Update messages
def updateMessage(x):
    msg['text'] = x


# Update Scores
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)


def updateComputerScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)


# Update choices
choices = ['rock', 'paper', 'scissor']


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == 'rock':
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == 'rock':
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    winlose(x, compChoice)


# Update Winner-Loser
def winlose(player, computer):
    if player == computer:
        updateMessage('Its a tie!!!')
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'paper':
        if computer == 'scissor':
            updateMessage('You loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'scissor':
        if computer == 'rock':
            updateMessage('You loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()


# Buttons
rock = Button(root, width=20, height=2, text='ROCK', bg='#FF3E4D', fg='white',
              command=lambda: updateChoice('rock'))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text='PAPER', bg='#FAD02E', fg='white',
               command=lambda: updateChoice('paper'))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text='SCISSORS', bg='#0ABDE3', fg='white',
                 command=lambda: updateChoice('scissor'))
scissor.grid(row=2, column=3)

root.mainloop()
