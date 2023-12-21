import tkinter
from tkinter import  messagebox
import password_generator
# for copy and paste
import pyperclip
import json

FONT = "Courier"

# search website

def find_password():
    website = website_input.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showerror(title="error",message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\n Password = {password}")
        else:
            messagebox.showerror(title="Error",message="Match Not Found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator_button_clicked():
    password = password_generator.password()
    genrated_password = password.generate()
    password_input.insert(0,genrated_password)
    pyperclip.copy(genrated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website_entry = website_input.get()
    user_entry = user_input.get()
    password_entry = password_input.get()
    new_data = {website_entry:{
        "email":user_entry,
        "password":password_entry
    }}


    if website_entry=="" or user_entry=="" or password_entry=="":
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \n Email: {user_entry}\n password: {password_entry}\n Is it ok to save? ")
        # if is_ok:

            # with open("data.txt","a") as file:
            #     file.write(f"Website:{website_entry} | Email/Username: {user_entry} | Password : {password_entry} "+"\n")
        try:
            with open("data.json","r") as file:
                # reading old data
                data =json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            # updating  new data
            data.update(new_data)
            with open("data.json", 'w') as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)
            website_input.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = tkinter.Canvas(height=200,width=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

# user personal info labels

website = tkinter.Label(text="Website :",pady=8)
website.grid(row=1,column=0)
user = tkinter.Label(text="Email/Username :",pady=8)
user.grid(row=2,column=0)
password = tkinter.Label(text="Password :",pady=8)
password.grid(row=3,column=0)


# user personal info. entries..
website_input = tkinter.Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

user_input = tkinter.Entry(width=51)
user_input.grid(row=2, column=1,columnspan=2)
user_input.insert(0,"drishti@gmail.com")

password_input = tkinter.Entry(width=33)
password_input.grid(row=3, column=1)


# generate password button
genrate_pw_button= tkinter.Button(text="Generate Password",width=13,command=pw_generator_button_clicked)
genrate_pw_button.grid(row=3,column=2)
# add button
add_button = tkinter.Button(text="Add",width=43,command=add_button_clicked)
add_button.grid(row=4,column=1,columnspan=2)
# search button
search_button = tkinter.Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)
window.mainloop()