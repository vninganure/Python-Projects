from tkinter import *

window = Tk()
window.title("Miles to Km")

def calculate_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    my_label_ans.config(text=f"{km}")


# Label
my_label = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label.grid(row= 1, column=0)

my_label_ans = Label(text=0, font=("Arial", 12, "bold"))
my_label_ans.grid(row= 1, column=1)

my_label_miles = Label(text="Miles", font=("Arial", 12, "bold"))
my_label_miles.grid(row= 0, column=2)

my_label_km = Label(text="Km", font=("Arial", 12, "bold"))
my_label_km.grid(row= 1, column=2)



#button

def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)

button = Button(text="calculate", command=calculate_to_km)
button.grid(row=2, column=1)

# Entry

entry = Entry(width=10)
entry.grid(row=0, column=1)







window.mainloop()