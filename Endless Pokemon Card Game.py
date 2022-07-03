# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:48:51 2022

@author: Swasti
"""

from tkinter import*
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Pokemon Card Game")
root.geometry("600x400")
root.configure(background = "orange")

pikachu = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/pikachu.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_score = Label(root, bg = "royal blue", fg = "white")
player1_score.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_score = Label(root, bg = "royal blue", fg = "white")
player2_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_pikachu_label = Label(root, bg = "yellow", fg = "black")
random_pikachu_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()