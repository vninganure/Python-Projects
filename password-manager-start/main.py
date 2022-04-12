from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website:
            {"email": email,
             "password": password
             }}

    if len(website) == 0 and len(password) == 0:
        not_ok = messagebox.showinfo(title="Oops", message="Please make sure you havn't left anything ")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Here are the entered details:\nwebsite: {website}:\nPassword: {password}\nis it ok to add?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # read json file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # create file
                    json.dump(new_data, data_file, indent=4)
            else:
                # update data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # create file
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="details",
                            message="NO data found, please add the data in it.")
    else:
        if website in data:
            messagebox.showinfo(title="details",
                                message=f"email:{data[website]['email']}\nPassword: {data[website]['password']}\n")
        else:
            messagebox.showinfo(title="details",
                                message="No data found")

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entry
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vjsmvit@gmail.com")
pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=1, columnspan=2)

# Button
gen_pass_button = Button(text="Generate Password", command=generate_password, width=17)
gen_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=17, command=find_password)
search_button.grid(row=1, column=2)

windows.mainloop()
