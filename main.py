from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main Window:
root = Tk()
root.title('Rock-Paper-Scissors')
root.minsize(860, 300)
root.maxsize(860, 300)
root.configure(background='#9b59b6')

# Pictures:
# Importing all Pictures to variables.
rock_img = ImageTk.PhotoImage(Image.open('rock-user.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper-user.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissors-user.png'))
rock_img_comp = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img_comp = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img_comp = ImageTk.PhotoImage(Image.open('scissors.png'))

# Insert Pictures:
# Using the picture variables as labels.
user_label = Label(root, image=scissor_img, bg='#9b59b6')
comp_label = Label(root, image=scissor_img_comp, bg='#9b59b6')
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores:
# The scores will be showed in a label which we will update using function update Scores.
playerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators:
# Indicator label will indicate on the left side we got computers move and on the right side we got users move.
user_indicator = Label(root, font=50, text='USER', bg='#9b59b6', fg='white')
comp_indicator = Label(root, font=50, text='COMPUTER', bg='#9b59b6', fg='white')
comp_indicator.grid(row=0, column=1)
user_indicator.grid(row=0, column=3)

# Messages:
# Message will show up below the buttons declaring the results of the game.
msg = Label(root, font=50, bg='#9b59b6', fg='white')
msg.grid(row=3, column=2)

# Update messages:
# Update message parameter x carries the result in words of the game just played, it will be displayed just below the buttons.
def updateMessage(x):
    msg['text'] = x


# Update Scores:
# Update Scores function will add 1 to the previous score when any one of the function is directly called.
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)


def updateComputerScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)


# Update choices:
choices = ['rock', 'paper', 'scissor']


def updateChoice(x):                     # x will be the users move inputted using the buttons
    # for computer
    compChoice = choices[randint(0, 2)]  # computer will choose its move in a constraint of 3 choices, randomly using randint
    if compChoice == 'rock':             # and accordingly we will show the choice of the computer on the left label
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == 'rock':                      # when a user chooses, we have to show users choice on the right label
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    winlose(x, compChoice)               # after both parties have chosen their moves, we need to find the results


# Update Winner-Loser:
# Update the Results depending on the choices one's make, and according to the rules of the game, the winner will be decided.
def winlose(player, computer):
    if player == computer:
        updateMessage('Its a tie!!!')   # when it's a tie, we won't update the winning of neither player on the scoreboard
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You loose')  # the result of the game in words will be shown on the screen 
            updateComputerScore()       # we will only update the scoreboard number of the winning side
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


# Buttons:
# Buttons used for declaring users move, and sending users move to updateChoice function to compare the choices of computer vs. user and respectively updating Scores.
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
