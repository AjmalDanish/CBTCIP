import tkinter as tk
import tkinter.ttk as ttk
import webview
from tkinter import messagebox
import random
from pyfiglet import figlet_format as f_form
from termcolor2 import colored

def play_game():
    global user1_Score, user2_Score
    randomChoose = random.choice(["ROCK", "PAPER", "SCISSORS"])

    user1 = user_choice.get().upper()
    result_text.delete(1.0, tk.END)  
    result_text.insert(tk.END, f"Computer chose {randomChoose}\n")

    if user1 == "Q":
        root.quit()
    elif user1 == randomChoose:
        result_text.tag_configure("black", foreground="black",background="yellow")
        result_text.insert(tk.END, f_form("No one wins!"), "black")
    elif user1 == "ROCK":
        if randomChoose == "PAPER":
            result_text.tag_configure("red", foreground="yellow",background="blue")
            result_text.insert(tk.END, f_form("Computer wins"), "red")
            user2_Score += 1
        elif randomChoose == "SCISSORS":
            result_text.tag_configure("green", foreground="green",background="yellow")
            result_text.insert(tk.END, f_form("You win"), "green")
            user1_Score += 1
    elif user1 == "PAPER":
        if randomChoose == "ROCK":
            result_text.tag_configure("green", foreground="red",background="green")
            result_text.insert(tk.END, f_form("You win"), "green")
            user1_Score += 1
        elif randomChoose == "SCISSORS":
            result_text.tag_configure("red", foreground="red",background="yellow")
            result_text.insert(tk.END, f_form("Computer wins"), "red")
            user2_Score += 1
    elif user1 == "SCISSORS":
        if randomChoose == "ROCK":
            result_text.tag_configure("red", foreground="red",background="light blue")
            result_text.insert(tk.END, f_form("Computer wins"), "red")
            user2_Score += 1
        elif randomChoose == "PAPER":
            result_text.tag_configure("green", foreground="green",background="yellow")
            result_text.insert(tk.END, f_form("You win"), "green")
            user1_Score += 1
    else:
        result_text.tag_configure("black", foreground="white",background="black")
        result_text.insert(tk.END, f_form("Error!"), "black")

    score_label.config(text=f"Your Score: {user1_Score}\nComputer Score: {user2_Score}")

    if user1_Score == gameRound and gameRound != 0:
        messagebox.showinfo("Game Over", "You win!")
        root.quit()
    elif user2_Score == gameRound and gameRound != 0:
        messagebox.showinfo("Game Over", "Computer wins!")
        root.quit()

root = tk.Tk()
root.title("Rock Paper Scissors Game")

user_choice = tk.StringVar()

game_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Helvetica", 16))
game_label.pack(pady=10)

rules_label = tk.Label(root, text="Game Rules:\n\n- You are playing against the computer.\n- Choose ROCK, PAPER, or SCISSORS by typing the respective option.\n- You can type Q to quit the game.\n- The game will be played for a total of 3 rounds.\n- The player with the most wins after 3 rounds wins the game.\n\nEnter your choice:")
rules_label.pack()

user_entry = tk.Entry(root, textvariable=user_choice)
user_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_text = tk.Text(root, wrap=tk.WORD, height=8, width=70)
result_text.pack()

score_label = tk.Label(root, text="Your Score: 0\nComputer Score: 0")
score_label.pack()

user1_Score = 0  
user2_Score = 0  
gameRound = 3    

root.mainloop()
