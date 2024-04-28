from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")
curr_card = {}


def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = choice(to_learn)
    canvas.itemconfigure(card_bg_img, image=card_front_img)
    canvas.itemconfigure(card_title, text="French", fill="black")
    canvas.itemconfigure(card_word, text=curr_card['French'], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfigure(card_bg_img, image=card_back_img)
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=curr_card['English'], fill="white")


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_bg_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
check_img = PhotoImage(file='images/right.png')
known_button = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
known_button.config(padx=50, pady=50)
known_button.grid(column=0, row=1)
flip_timer = window.after(3000, flip_card)
wrong_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(column=1, row=1)
next_card()
window.mainloop()
