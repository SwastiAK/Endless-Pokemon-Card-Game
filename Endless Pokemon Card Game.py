# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:48:51 2022

@author: Swasti
"""

from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()

root.title("Endless Pokemon Game")
root.geometry("620x460")

root.configure(background = "orange")

abra = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/button.jpg"))
charmender = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/Pokemon_Images_students/squirtle.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_pc_label = Label(root, bg = "white", fg = "orange")
random_pc_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = [pikachu, bulbasour, iyvasour, charmender, squirtle, ratata, jigglypuff, meowth, persion, abra, kadabra]

power_list = [200,60,100,50,50,40,70,60,70,30,70]

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = [pokemon]
power_list = [200]
label["image"] = random_pokemon

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list [random_no]
    label["image"] = random_pokemon
    
    random_power_list = power_list[random_no]
    player1_score = player1_score + random_power_list
    
player1_btn = Button(root, image = img, command = player1)
player1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_score = 0
def player2():
    global player2_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list [random_no]
    label["image"] = random_pokemon
    
    random_power_list = power_list[random_no]
    player2_score = player2_score + random_power_list
    
player2_btn = Button(root, image = img, command = player2)
player2_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

root.mainloop()