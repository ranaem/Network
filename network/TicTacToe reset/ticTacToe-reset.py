"""
Created on Sat May 11 14:52:28 2024

@author: ranaemad
"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(" Tic-Tac-Toe ")
window.geometry("400x300")

lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

turn = 1  # For first person turn.

# Function for Buttons
def clicked(btn):
    global turn
    if btn["text"] == " ":
        if turn == 1:
            turn = 2
            btn["text"] = "X"
        else:
            turn = 1
            btn["text"] = "O"
        check()

# Reset the game to start all over again
def reset():
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn["text"] = " "


flag = 1 # To check if the game is finished without any side winning or not

def check():
    global flag
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
    for i in range(0, 9, 3):
        # row
        if buttons[i]["text"] == buttons[i+1]["text"] == buttons[i+2]["text"] != " ":
            win(buttons[i]["text"])
    for i in range(3):
        # column
        if buttons[i]["text"] == buttons[i+3]["text"] == buttons[i+6]["text"] != " ":
            win(buttons[i]["text"])
    # right diagonal
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != " ":
        win(buttons[0]["text"])
    # left diagonal
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != " ":
        win(buttons[2]["text"])
    flag += 1
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        # dont destroy to use reset button

def win(player):
    ans = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", ans)
    # dont destroy to play many matches

# create the buttons for the game
buttons = []
for i in range(3):
    for j in range(3):
        btn = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'))
        btn.grid(column=j+1, row=i+1)
        btn.config(command=lambda btn=btn: clicked(btn))
        buttons.append(btn)

# creating a reset button
resetbtn = Button(window, text="\nRESET\n", height=2, bg="yellow", fg="black", command=reset)
resetbtn.grid(row=5, column=2, pady=20)

# assign buttons to their variables
btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9 = buttons

window.mainloop()
