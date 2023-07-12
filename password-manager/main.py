import string
from tkinter import *
from tkinter import messagebox
from random import randint
import pyperclip
import json

PASSWORD_LENGTH = 20
EMAIL = "myemail@email.com"
PASSWORD_FILE = "data.json"

# -- Password Generator -- #

def generate_password():
    random_letters = string.ascii_letters + string.digits + string.punctuation

    password = "".join([random_letters[randint(0, len(random_letters) - 1)] for _ in range(0, PASSWORD_LENGTH)])

    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# -- Save Password -- #
def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        },
    }

    if website.strip() == "" or email_username.strip() == "" or password.strip() == "":
        messagebox.showerror(message="Please don't leave any fields empty!")
    else:
        # try opening an existing file
        try:
            with open(PASSWORD_FILE, "r") as file:
                contents = json.load(file)

        # if no file exists, create new file
        except FileNotFoundError:
            with open(PASSWORD_FILE, "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            with open(PASSWORD_FILE, "w") as file:
                contents.update(new_data)
                json.dump(contents, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -- Search for Password -- #
def search_website():
    website = website_entry.get()

    # try opening file:
    try:
        with open(PASSWORD_FILE, "r") as file:
            contents = json.load(file)

        # search for website entered
        results = contents.get(website)

        if results is None:
            messagebox.showinfo(message="User name/password not found...")
        else:
            results_username = results["email"]
            results_password = results["password"]
            messagebox.showinfo(message=f"User Name: {results_username}\nPassword: {results_password}")

    except FileNotFoundError:
        messagebox.showinfo(message="User name/password not found")


# -- UI Setup -- #

screen = Tk()
screen.title("MyPass Password Manager")
screen.config(pady=20, padx=20)

# Logo
logo = Canvas(screen, width=200, height=200)
logo_image = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_image)
logo.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_name_label = Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)

email_username_entry = Entry(width=40)
email_username_entry.insert(0, EMAIL)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_button = Button(text="Generate Password", width=15, command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_website, width=15)
search_button.grid(column=2, row=1)

screen.mainloop()
