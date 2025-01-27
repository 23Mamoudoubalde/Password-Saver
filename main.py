from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(symbols) for _ in  range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left anything empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty dictionary
            data = {}
        except json.JSONDecodeError:
            # If the file is empty or has invalid JSON, start with an empty dictionary
            data = {}

        # Update the data with new entry
        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        web_entry.delete(0, END)
        password_entry.delete(0, END)

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message= f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title ="Error", message=f"No details for {website} existence")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Forteresse Digital")
window.config(padx=50,pady=50)
canvas = Canvas(width=200, height=200)
passcode_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=passcode_img)
canvas.grid(column=1,row=0)
web_label= Label(text= "Website: ")
web_label.grid(column=0,row=1)
web_entry = Entry(width=21)
web_entry.grid(column=1,row=1)
web_entry.focus()


email_label =Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=3)

email_entry.insert(0, "let_get_this_code@running.edu")

add_button = Button(text ="Add",width=36,command=save)
add_button.grid(row=4,column=1, columnspan=2)



password_label =Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text = "Generate Password", command=generate_password)
generate_password_button.grid(column=2, row= 3)

search_button = Button(text = "Search", width=15, command=find_password)
search_button.grid(column=2, row= 1)

#json file allow us to tap in to the net
#json.dump(), json.load(), json.update






window.mainloop()
