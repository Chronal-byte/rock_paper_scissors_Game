import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from game import Game

game=Game()

class game_GUI():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('Rock, Paper, Scissors!')
        #imgs for btns
        self.rock_img_original = Image.open('./img/Rock.png')
        self.paper_img_original = Image.open('./img/Paper.png')
        self.scissors_img_original = Image.open('./img/Scissors.png')
        self.rock_img_tk = ImageTk.PhotoImage(self.rock_img_original)
        self.paper_img_tk = ImageTk.PhotoImage(self.paper_img_original)
        self.scissors_img_tk = ImageTk.PhotoImage(self.scissors_img_original)
        #fonts
        self.font_Montserrat = font.Font(family='Montserrat',size=12,weight='bold')
        self.init_widgets()
        self.root.mainloop()

    def turns_section(self):
        self.turns_frame = tk.Frame(self.root)
        #computer turns
        self.computer_turn_frame = tk.Frame(self.turns_frame)
        self.computer_turn_label = tk.Label(self.computer_turn_frame,font=self.font_Montserrat,text='Computer Turn')
        self.computer_turn_field = tk.Entry(self.computer_turn_frame)
        self.computer_turn_label.pack(side='top')
        self.computer_turn_field.pack(side='top')
        self.computer_turn_frame.pack(side='left',padx=10)
        #user turns
        self.player_turn_frame = tk.Frame(self.turns_frame)
        self.player_turn_label = tk.Label(self.player_turn_frame,font=self.font_Montserrat,text='Player Turn')
        self.player_turn_field = tk.Entry(self.player_turn_frame)
        self.player_turn_label.pack(side='top')
        self.player_turn_field.pack(side='top')
        self.player_turn_frame.pack(side='left',padx=10)
        self.turns_frame.pack(side='top')

    def winner_section(self):
        self.winner_frame = tk.Frame(self.root)
        #winner field
        self.winner_label = tk.Label(self.winner_frame,font=self.font_Montserrat,text='Winner')
        self.winner_field = tk.Entry(self.winner_frame)
        self.winner_label.pack(side='top')
        self.winner_field.pack(side='top')
        self.winner_frame.pack(side='top',pady=10)

    def score_section(self):
        self.score_frame = tk.Frame(self.root)
        #computer score
        self.computer_score_frame = tk.Frame(self.score_frame)
        self.computer_score_label = tk.Label(self.computer_score_frame,font=self.font_Montserrat,text='Computer Score')
        self.computer_score_field = tk.Entry(self.computer_score_frame)
        self.computer_score_label.pack(side='top')
        self.computer_score_field.pack(side='top')
        self.computer_score_frame.pack(side='left',padx=10)
        #user score
        self.user_score_frame = tk.Frame(self.score_frame)
        self.user_score_label = tk.Label(self.user_score_frame,font=self.font_Montserrat,text='User Score')
        self.user_score_field = tk.Entry(self.user_score_frame)
        self.user_score_label.pack(side='top')
        self.user_score_field.pack(side='top')
        self.user_score_frame.pack(side='left',padx=10)

        self.score_frame.pack(side='top',pady=10)

    def select_section(self):
        #user btns
        self.select_frame = tk.Frame(self.root)
        self.rock_btn = tk.Button(self.select_frame,image=self.rock_img_tk,)
        self.paper_btn = tk.Button(self.select_frame,image=self.paper_img_tk)
        self.scissors_btn = tk.Button(self.select_frame,image=self.scissors_img_tk)
        self.rock_btn.pack(side='left',padx=10)
        self.paper_btn.pack(side='left',padx=10)
        self.scissors_btn.pack(side='left',padx=10)
        self.select_frame.pack(side='top',pady=10)

    def init_widgets(self):
        self.turns_section()
        self.winner_section()
        self.score_section()
        self.select_section()