from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
data_dict = {}


# ------------------------------READ DATA ----------------------------
try:
    data = pandas.read_csv("../data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("../data/french_words.csv")
df = pandas.DataFrame(data)
data_dict = data.to_dict(orient="records")



def next_card():
    global current_word, flip_card
    window.after_cancel(flip_card)
    current_word = choice(data_dict)
    canvas.itemconfig(next_lang, text="French", fill='black')
    canvas.itemconfig(next_word, text=current_word['French'], fill='black')
    canvas.itemconfig(canvas_image, image=french_image)
    flip_card = window.after(3000, func=flip_img)

def flip_img():
    canvas.itemconfig(next_lang, text="English", fill="white")
    canvas.itemconfig(next_word, text=current_word['English'], fill="white")
    canvas.itemconfig(canvas_image, image=english_image)

def is_known():
    data_dict.remove(current_word)
    print(len(data_dict))
    df = pandas.DataFrame(data_dict)
    df.to_csv("../data/words_to_learn.csv", index=False)
    next_card()




# ------------------------------UI SETUP----------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_card = window.after(3000, func=flip_img)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_image = PhotoImage(file="images/card_front.png")
english_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=french_image)
next_lang = canvas.create_text(400, 150, text="Text", font=("Arial", 40, "italic"))
next_word = canvas.create_text(400, 283,text="sfd", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

check_image = PhotoImage(file="../images/right.png")
known_button = Button(image=check_image,highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="../images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()




window.mainloop()
