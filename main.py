from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
translate_text = canvas.create_text(400, 150, text="French", font=('Ariel', 40))
lang_text = canvas.create_text(400, 263, text="trouve", font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
right_btn_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.config(padx=50, pady=50)
right_button.grid(column=0, row=1)

wrong_btn_img = PhotoImage(file='images/wrong.png')
right_button = Button(image=wrong_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1)
# my_image.pack()
# button.pack()
window.mainloop()
