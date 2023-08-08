import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

MAX_ATTEMPTS = 10

class PlayerVsComputerGame(tk.Toplevel):
    def __init__(self, parent, player_name):
        super().__init__(parent)
        self.title("Player vs Computer")
        self.parent = parent
        self.player_name = player_name
        self.computer_name = "Computer"
        self.player_num = None
        self.player_attempts = 0
        self.computer_num = None
        self.computer_attempts = 0

        self.create_widgets()
        self.new_game()


    def create_widgets(self):
        self.lbl_instructions = tk.Label(self, text=f"Computer sets a number for you to guess.\n{self.player_name} will guess the number.")
        self.lbl_instructions.pack()

        self.lbl_attempts = tk.Label(self, text="")
        self.lbl_attempts.pack()

        self.lbl_hint = tk.Label(self, text="")
        self.lbl_hint.pack()

        self.entry_guess = tk.Entry(self)
        self.entry_guess.pack()

        self.btn_guess = tk.Button(self, text="Guess", command=self.check_guess)
        self.btn_guess.pack()

    def new_game(self):
        self.player_num = random.randint(1000, 9999)
        self.player_attempts = 0
        self.computer_num = random.randint(1000, 9999)
        if self.computer_num is None:  # User clicked cancel or closed the dialog
            self.destroy()  # Exit the game
            return
        self.computer_attempts = 0
        self.show_instructions()

    def show_instructions(self):
        self.lbl_instructions.config(text=f"{self.player_name}, it's your turn to guess.")
        self.entry_guess.config(state=tk.NORMAL)
        self.btn_guess.config(state=tk.NORMAL)
        self.lbl_hint.config(text="")
        self.lbl_attempts.config(text=f"No. of attempts: {self.player_attempts}")

    def get_number_input(self, message):
        number_str = simpledialog.askstring("Number Input", message)
        try:
            number = int(number_str)
            if not (1000 <= number <= 9999):
                messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")
                return self.get_number_input(message)
            return number
        except (ValueError, TypeError):
            return None

    def check_guess(self):
        guess = self.entry_guess.get()
        try:
            player_guess = int(guess)
            if player_guess < 1000 or player_guess > 9999:
                messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid multi-digit number.")
            return

        self.player_attempts += 1

        if player_guess == self.player_num:
            messagebox.showinfo("Congratulations!", f"Congratulations! You guessed the number in {self.player_attempts} attempts!")
            self.entry_guess.config(state=tk.DISABLED)
            self.btn_guess.config(state=tk.DISABLED)
            self.computer_game()  # Call computer's turn after the player's turn
            self.createC_widgets()  # Create the widgets for the computer's turn
            self.newC_game()  # Start the computer's turn
            return

        matching_digits = self.get_matching_digits(self.player_num, player_guess)
        self.lbl_hint.config(text=f"Hints: {matching_digits} digits are correct.")
        self.lbl_attempts.config(text=f"No. of attempts: {self.player_attempts}")

        if self.player_attempts >= MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"Sorry, you couldn't guess the number within {MAX_ATTEMPTS} attempts. The number was {self.player_num}.")
            self.entry_guess.config(state=tk.DISABLED)
            self.btn_guess.config(state=tk.DISABLED)
            self.computer_game()  # Call computer's turn after the player's turn
            self.createC_widgets()  # Create the widgets for the computer's turn
            self.newC_game()  # Start the computer's turn
            return
        
    def createC_widgets(self):
        self.lbl_instructions = tk.Label(self, text=f"{self.player_name}, Set a 4-digit number for the computer to guess.")
        self.lbl_instructions.pack()

        self.lbl_attempts = tk.Label(self, text="")
        self.lbl_attempts.pack()

        self.lbl_hint = tk.Label(self, text="")
        self.lbl_hint.pack()

        self.entry_number = tk.Entry(self)
        self.entry_number.pack()

        self.btn_setC_number = tk.Button(self, text="Set Number", command=self.setC_number)
        self.btn_setC_number.pack()

    def newC_game(self):
        self.player_num = None
        self.player_attempts = 0
        self.computer_num = None
        self.computer_attempts = 0
    def setC_number(self):
        number_str = self.entry_number.get()
        try:
            self.lbl_instructions.config(text=f"{self.computer_name} is guessing your number.")
            self.lbl_hint.config(text="")
            self.lbl_attempts.config(text="Computer's Attempts: 0")
            self.player_num = int(number_str)
            if not (1000 <= self.player_num <= 9999):
                messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")
                return
            self.entry_number.config(state=tk.DISABLED)
            self.btn_setC_number.config(state=tk.DISABLED)
            self.computer_game()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")        
    def computer_game(self, player_num=None):  # Make player_num optional with default value None
        if player_num is not None:
            self.player_num = player_num  # Set the player_num before the computer's turn
        self.computer_num = random.randint(1000, 9999)
        self.computer_attempts = 0
        self.after(1000, self.computer_guess)

    def computer_guess(self):
        if self.player_num is None:
            return
        self.computer_attempts += 1
        if self.computer_attempts > MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"Sorry, {self.computer_name} couldn't guess your number within {MAX_ATTEMPTS} attempts. The number was {self.player_num}.")
            self.newC_game()            
            self.show_result()
            self.destroy()
            return

        computer_guess = random.randint(1000, 9999)

        # Ensure that computer_guess is a 4-digit number
        while computer_guess < 1000 or computer_guess > 9999:
            computer_guess = random.randint(1000, 9999)

        if computer_guess == self.player_num:
            messagebox.showinfo("Congratulations!", f"{self.computer_name} guessed your number ({self.player_num}) in {self.computer_attempts} attempts!")
            self.newC_game()            
            self.show_result()
            self.destroy()
            return

        matching_digits = self.get_matching_digits(self.player_num, computer_guess)
        self.lbl_hint.config(text=f"Hints: {matching_digits} digits are correct.")
        self.lbl_attempts.config(text=f"Computer's Attempts: {self.computer_attempts}")
        self.after(1000, self.computer_guess)
            # Check the game result after the computer's last attempt
    def show_result(self):
        if self.computer_attempts == 10 and self.player_attempts == 10:
            messagebox.showinfo("MAstermind!", "It's a tie!")
        elif self.computer_attempts == self.player_attempts:
            messagebox.showinfo("Mastermind!", "It's a tie!")
        elif self.computer_attempts < self.player_attempts:
            messagebox.showinfo("Mastermind!", f"{self.computer_name} is the Mastermind!")
        else:
            messagebox.showinfo("Mastermind!", f"{self.player_name} is the Mastermind!")

    def get_matching_digits(self, secret, guess):
        secret_digits = [int(digit) for digit in str(secret)]
        guess_digits = [int(digit) for digit in str(guess)]
        return sum(s == g for s, g in zip(secret_digits, guess_digits))
    

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        
        self.game_mode = tk.StringVar()
        self.player_name = tk.StringVar()
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Mastermind Rules:").pack()
        tk.Label(self.root, text="1. The code-setter selects a secret 4-digit number.").pack()
        tk.Label(self.root, text="2. The code-guesser tries to guess the number within 10 attempts.").pack()
        tk.Label(self.root, text="3. After each guess, the code-setter gives hints on correct digits and positions.").pack()
        tk.Label(self.root, text="4. Guess correctly within 10 attempts to win.").pack()
        tk.Label(self.root, text="5. The roles switch, and the game continues.").pack()
        tk.Label(self.root, text="6. The player with more wins is the ultimate Mastermind!").pack()
        tk.Label(self.root, text="7. Have fun and good luck!").pack()
        
        tk.Label(self.root, text="Let's play Mastermind!").pack()
        tk.Label(self.root, text="Choose the game mode:").pack()
        self.game_mode = tk.StringVar()
        self.game_mode.set("pvsc")
        
        tk.Radiobutton(self.root, text="Player vs Computer", variable=self.game_mode, value="pvsc").pack()
        tk.Radiobutton(self.root, text="Player vs Player", variable=self.game_mode, value="pvsp").pack()
        
        tk.Button(self.root, text="Start Game", command=self.start_game).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def start_game(self):
        mode = self.game_mode.get()
        
        if mode == "pvsc":
            self.player_name.set("")
            player_name = simpledialog.askstring("Player Name", "Enter Player name:")
            if player_name is None:  # User clicked cancel or closed the dialog
                return
            PlayerVsComputerGame(self.root, player_name)
        elif mode == "pvsp":
            self.player1_name.set("")
            self.player2_name.set("")
            player1_name = simpledialog.askstring("Player 1 Name", "Enter Player 1's name:")
            if player1_name is None:  # User clicked cancel or closed the dialog
                return
            player2_name = simpledialog.askstring("Player 2 Name", "Enter Player 2's name:")
            if player2_name is None:  # User clicked cancel or closed the dialog
                return
            self.player_vs_player(player1_name, player2_name)
    
    def player_vs_player(self, player1_name, player2_name):
        player2_num = self.get_number_input(f"{player2_name}, set a 4-digit number for {player1_name} to guess.")
        if player2_num is None:  # User clicked cancel or closed the dialog
            return
        player1_attempts = 0

        while player1_attempts < MAX_ATTEMPTS:
            player1_guess = self.get_number_input(f"{player1_name}, it's your turn to guess {player2_name}'s number.")
            if player1_guess is None:  # User clicked cancel or closed the dialog
                return
            player1_attempts += 1

            if player1_guess == player2_num:
                messagebox.showinfo("Congratulations!", f"Congratulations! {player1_name} guessed the number in {player1_attempts} attempts!")
                break

            matching_digits = self.get_matching_digits(player2_num, player1_guess)
            messagebox.showinfo("Hints", f"{matching_digits} digits are correct.")
        
        if player1_attempts >= MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"Sorry, {player1_name} couldn't guess the number within {MAX_ATTEMPTS} attempts. The number was {player2_num}.")

        player1_num = self.get_number_input(f"{player1_name}, set a 4-digit number for {player2_name} to guess.")
        if player1_num is None:  # User clicked cancel or closed the dialog
            return
        player2_attempts = 0

        while player2_attempts < MAX_ATTEMPTS:
            player2_guess = self.get_number_input(f"{player2_name}, it's your turn to guess {player1_name}'s number.")
            if player2_guess is None:  # User clicked cancel or closed the dialog
                return
            player2_attempts += 1

            if player2_guess == player1_num:
                messagebox.showinfo("Congratulations!", f"Congratulations! {player2_name} guessed the number in {player2_attempts} attempts!")
                break

            matching_digits = self.get_matching_digits(player1_num, player2_guess)
            messagebox.showinfo("Hints", f"{matching_digits} digits are correct.")
        
        if player2_attempts >= MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"Sorry, {player2_name} couldn't guess the number within {MAX_ATTEMPTS} attempts. The number was {player1_num}.")

        if player1_attempts == player2_attempts:
            messagebox.showinfo("It's a Tie!", "It's a tie!")
        elif player1_attempts < player2_attempts:
            messagebox.showinfo("Mastermind!", f"{player1_name} is the Mastermind!")
        else:
            messagebox.showinfo("Mastermind!", f"{player2_name} is the Mastermind!")

    def get_number_input(self, message):
        num_str = simpledialog.askstring("Number Input", message)
        if num_str is None:  # User clicked cancel or closed the dialog
            self.root.destroy()  # Exit the game
        try:
            num = int(num_str)
            if 1000 <= num <= 9999:
                return num
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")
                return self.get_number_input(message)  # Ask for input again
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid multi-digit number.")
            return self.get_number_input(message)  # Ask for input again



    def get_matching_digits(self, secret, guess):
        secret_digits = [int(digit) for digit in str(secret)]
        guess_digits = [int(digit) for digit in str(guess)]
        return sum(s == g for s, g in zip(secret_digits, guess_digits))

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
