# Import Modules
from tkinter import *
from tkinter import messagebox
import random


#---------------------------- DEFINING FUNNCTIONS ----------------------------#

def reset():
    global player
    for row in range(3):
        for column in range(3):
            buttons[row][column]["text"] = " "
            buttons[row][column]["state"] = NORMAL
    player = random.choice(players)

def change_player():
    global player 
    for symbol in players:
        if player!= symbol:
            player = symbol
            break

def check_winner():
    for k in range(3):
        if (buttons[k][0]["text"] == buttons[k][1]["text"] ==buttons[k][2]["text"] == player or buttons[0][k]["text"] == buttons[1][k]["text"] == buttons[2][k]["text"] == player):
            messagebox.showinfo(title="Game Over", message=f"Tic Tac Toe! {player} has won.")
            reset()
    if (buttons[0][0]["text"] == buttons[1][1]["text"] ==buttons[2][2]["text"] == player or buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player):
            messagebox.showinfo(title="Game Over", message=f"Tic Tac Toe! {player} has won.")
            reset()
    elif (buttons[0][0]["state"] == buttons[0][1]["state"] ==buttons[0][2]["state"] == buttons[1][0]["state"] == buttons[1][1]["state"] == buttons[1][2]["state"] == buttons[2][0]["state"] == buttons[2][1]["state"] == buttons[2][2]["state"] == DISABLED):
            messagebox.showinfo(title="Game Over", message="Tied! The match ended in a draw")
            reset()

def click_button(row, column):
    buttons[row][column].config(text=player, state=DISABLED, disabledforeground=colour[player])
    check_winner()
    change_player()
    chance_label.config(text=f"{player}'s chance", fg=colour[player])


#---------------------------- UI SETUP ----------------------------#

window = Tk()
window.title("Tic Tac Toe")
window.config(width=600, height=600, padx=20, pady=20, bg="#B2B1B9")
window.resizable(width=False, height=False)

players = ["X", "O"]
player = random.choice(players)

colour={"X":"#0A043C","O":"#DA0037"}

# positioning the buttons
frame = Frame(window)
frame.grid(row=0, column=0)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, width=6, height=3, bg="#EEEEEE", font=("Ariel", 22,"bold"),command=lambda row=row, column=column: click_button(row,column))
        buttons[row][column].grid(row=row, column=column)
    
chance_label = Label(text=f"{player}'s chance", font=("Courel", 15, "bold"), fg=colour[player],bg="#B2B1B9")
chance_label.grid(row=1, column=0)

window.mainloop()

