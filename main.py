from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR -------------------------------

def passgen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using list comprehension, the respective list runs based on loop numbers

    nr_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = nr_letters + nr_numbers + nr_symbols
    random.shuffle(password_list)

    pas = "".join(password_list)

    password_text.delete(0, END)
    password_text.insert(0, pas)

    # this pyper clip is when a password is generate it is stored in clipboard automatically
    pyperclip.copy(pas)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def savefile():
    website = str(web_text.get())
    username = str(username_text.get())
    password = str(password_text.get())

    new_data = {website: {"username":username, "password":password}}

    if website != "" and username != "" and password != "":
        validation = messagebox.askyesno(title="website", message = "Do you want to Save?")
        if validation:
            # creation of json object
            with open("password.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                    data.update(new_data)
                except:
                    with open("password.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    with open("password.json", "w") as data_file:
                        json.dump(data,data_file, indent=4)

            web_text.delete(0, END)
            password_text.delete(0, END)
            username_text.delete(0, END)

    else:
        messagebox.showerror("Alert", "Website or Username or Password is blank")


def search():
    with open("password.json", "r") as data_file:
        data = json.load(data_file)
        website = web_text.get()

        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo("Message", message = f"username is {username} and password is {password}")
        else:
            messagebox.showinfo("Message", message=f"No entries Found for {website}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(height = 200, width = 200)
window.config(padx = 40, pady = 40)

# Image importing

canvas = Canvas(width = 200, height = 224)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100,  image = logo)
canvas.grid(row = 1, column = 2)

# Website label and text box

website = Label()
website.config(text="Website")
website.grid(row = 2, column = 1, sticky = W)

web_text = Entry(width=15)
web_text.focus()
web_text.grid(row = 2, column = 2, sticky =W)

username = Label()
username.config(text="Email/Username")
username.grid(row = 3, column = 1, sticky = W)

username_text = Entry(width=30)
username_text.grid(row = 3, column = 2)

password = Label()
password.config(text="password")
password.grid(row = 4, column = 1, sticky = W)

password_text = Entry(width=15)
password_text.grid(row = 4, column = 2, sticky = W)

#calls pass() when pressed
2
new_pass.grid(row = 4, column = 2, sticky = E)

#calls addfile() when pressed
add_pass = Button(text="Add to File", command=savefile, width = 31)
add_pass.grid(row = 5, column = 2)

# calls Search() when pressed
search = Button(text="Search", command=search, width =14)
search.grid(row = 2, column = 2, sticky = E)


window.mainloop()