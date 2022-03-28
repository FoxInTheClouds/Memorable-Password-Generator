import tkinter as tk
from tkinter import ttk, IntVar, StringVar
from ctypes import windll
from pwned_check import pwned_check
import source_gen
import pyperclip
import sys
import os

os.chdir(sys._MEIPASS)  # This line makes sure that the program can find non python files

class DevNull:
    def write(self, msg):
        pass


#sys.stderr = DevNull()  # Supresses error messages

windll.shcore.SetProcessDpiAwareness(1)  # Makes the text not blurry

length = 15

root = tk.Tk()
root.update_idletasks()

root.resizable(False, False)
root.title("Password Generator")
root.configure(bg="#DBF3FA")
root.iconbitmap("logo.ico")

random_password = StringVar()
random_password.set("Password goes here")
memorable_password = StringVar()
memorable_password.set("Password goes here")

header = ttk.Label(
    root, 
    text="Creating Memorable Passwords", 
    style="Heading.TLabel")

header.grid(column=2, columnspan=3, row=0, padx="15", pady="15")

random_frame = ttk.Frame(root)
random_frame.grid(column=2, row=1, padx=15, pady=15)

random_password_box = ttk.Entry(
    random_frame, 
    textvariable=random_password, 
    state="readonly", 
    font=("Open Sans", 15), 
    cursor="arrow")

random_password_box.grid(column=0, row=0)

random_scroll = ttk.Scrollbar(
    random_frame, 
    orient='horizontal', 
    command=random_password_box.xview)

random_password_box.config(xscrollcommand=random_scroll.set)
random_scroll.grid(column=0, row=1, sticky="ew")

random_button = ttk.Button(root, text="Generate Random")
random_button.grid(column=1, row=1)


def show_random_password(
        length, 
        include_uppercase, 
        include_numbers, 
        include_symbols):

    secure = False
    while secure == False:
        new_random_password = source_gen.random_based_generator(
            length, 
            include_uppercase, 
            include_numbers, 
            include_symbols)
      
        if use_pwned_check.get() == 0:
            secure = True
        else:
            secure = pwned_check(new_random_password)

    random_password.set(new_random_password)

    random_password_box.config(textvariable=random_password)

    random_copy_text.set("Copy")


random_button.config(
    command=lambda: show_random_password(
        length.get(), 
        include_uppercase.get(), 
        include_numbers.get(), 
        include_symbols.get()))


def copy_random_password():
    pyperclip.copy(random_password.get())

    random_copy_text.set("Copied!")
 

random_copy_text = StringVar()
random_copy_text.set("Copy")

random_copy_button = ttk.Button(
    root,
    textvariable=random_copy_text, 
    command=copy_random_password)

random_copy_button.grid(column=3, row=1)

memorable_frame = ttk.Frame(root)
memorable_frame.grid(column=2, row=2, padx=15, pady=15)

memorable_password_box = ttk.Entry(
    memorable_frame, 
    textvariable=memorable_password, 
    state="readonly", 
    font=("Open Sans", 15), 
    cursor="arrow")

memorable_password_box.grid(column=0, row=0)

memorable_scroll = ttk.Scrollbar(
    memorable_frame, 
    orient='horizontal', 
    command=memorable_password_box.xview)

memorable_password_box.config(xscrollcommand=memorable_scroll.set)
memorable_scroll.grid(column=0, row=1, sticky="ew")

memorable_button = ttk.Button(root, text="Generate Memorable")
memorable_button.grid(column=1, row=2)


def show_memorable_password(
        word_number,
        include_uppercase,
        include_numbers,
        include_symbols,
        uppercase_position,
        numbers_position,
        symbols_position):

    secure = False
    while secure == False:
        new_memorable_password = source_gen.word_based_generator(
            word_number, 
            include_uppercase, 
            include_numbers, 
            include_symbols, 
            uppercase_position, 
            numbers_position, 
            symbols_position)

        if use_pwned_check.get() == 0:
            secure = True
        else:
            secure = pwned_check(new_memorable_password)

    memorable_password.set(new_memorable_password)
    memorable_password_box.config(textvariable=memorable_password)

    memorable_copy_text.set("Copy")


memorable_button.config(
    command=lambda: show_memorable_password(
        word_number.get(), 
        include_uppercase.get(), 
        include_numbers.get(), 
        include_symbols.get(), 
        uppercase_position.get(), 
        numbers_position.get(), 
        symbols_position.get()))


def copy_memorable_password():
    pyperclip.copy(memorable_password.get())

    memorable_copy_text.set("Copied!")


memorable_copy_text = StringVar()
memorable_copy_text.set("Copy")

memorable_copy_button = ttk.Button(
    root, 
    textvariable=memorable_copy_text, 
    command=copy_memorable_password)

memorable_copy_button.grid(column=3, row=2)


def valid_length():   
    if length.get() < 3 or length.get() > 20:       
        length.set(15)


length = IntVar()
length.set(15)

length_label = ttk.Label(root, text="Password length:")
length_label.grid(column=4, row=1, padx="15", pady="15")

length_input = ttk.Entry(
    root, 
    textvariable=length, 
    validate="all", 
    validatecommand=valid_length)

length_input.grid(column=5, row=1, padx="15", pady="15")


def valid_word_number():
    if word_number.get() < 2 or word_number.get() > 10:
        word_number.set(5)


word_number = IntVar()
word_number.set(5)

word_number_label = ttk.Label(root, text="Number of words:")
word_number_label.grid(column=4, row=2, padx="15", pady="15") 

word_number_input = ttk.Entry(
    root, 
    textvariable=word_number, 
    validate="focusout", 
    validatecommand=valid_word_number)

word_number_input.grid(column=5, row=2, padx="15", pady="15")

##############################

uppercase_frame = ttk.Frame(root)
uppercase_frame.grid(column=1, row=3, padx=15, pady=15, columnspan=2)

include_uppercase = tk.IntVar()
include_uppercase.set(1)

uppercase_letters = ttk.Checkbutton(
    uppercase_frame, 
    text="Include uppercase letters", 
    variable=include_uppercase, 
    onvalue=1, 
    offvalue=0)

uppercase_letters.grid(column=0, row=0, padx="15", pady="15", columnspan=2)

uppercase_position = tk.IntVar()
uppercase_position.set(1)

uppercase_position_input = ttk.Entry(
    uppercase_frame, 
    textvariable=uppercase_position)

uppercase_position_input.grid(column=1, row=1, padx="15", pady="15")

uppercase_position_input_text = ttk.Label(
    uppercase_frame, 
    text="Uppercase position:")

uppercase_position_input_text.grid(column=0, row=1, padx="15", pady="15")

###############################

numbers_frame = ttk.Frame(root)
numbers_frame.grid(column=3, row=3, padx="15", pady="15", columnspan=3)

include_numbers = tk.IntVar()
include_numbers.set(0)

numbers_box = ttk.Checkbutton(
    numbers_frame, 
    text="Include numbers", 
    variable=include_numbers, 
    onvalue=1, 
    offvalue=0)

numbers_box.grid(column=0, row=0, padx="15", pady="15", columnspan=2)

numbers_position = tk.IntVar()
numbers_position.set(2)

number_position_input = ttk.Entry(numbers_frame, textvariable=numbers_position)
number_position_input.grid(column=1, row=1, padx="15", pady="15")

number_position_input_text = ttk.Label(numbers_frame, text="Number position:")
number_position_input_text.grid(column=0, row=1, padx="15", pady="15")

##############################

symbols_frame = ttk.Frame(root)
symbols_frame.grid(column=1, row=4, padx="15", pady="15", columnspan=2)

include_symbols = tk.IntVar()
include_symbols.set(0)

symbols_box = ttk.Checkbutton(
    symbols_frame, 
    text="Include symbols", 
    variable=include_symbols, 
    onvalue=1, 
    offvalue=0)

symbols_box.grid(column=0, row=0, padx="15", pady="15", columnspan=2)

symbols_position = tk.IntVar()
symbols_position.set(2)

symbol_position_input = ttk.Entry(symbols_frame, textvariable=symbols_position)
symbol_position_input.grid(column=1, row=1, padx="15", pady="15")

symbol_position_input_text = ttk.Label(symbols_frame, text="Symbol position:")
symbol_position_input_text.grid(column=0, row=1, padx="15", pady="15")


##############################

pwned_check_frame = ttk.Frame(root)
pwned_check_frame.grid(column=1, row=5, padx="15", pady="15", columnspan=5)

pwned_check_text = ttk.Label(
    pwned_check_frame, 
    text="Check if your password has been in a data breach:")

pwned_check_text.grid(column=0, row=0, padx="15", pady="15", columnspan=2)

inputted_password = tk.StringVar()
inputted_password.set("example123")

pwned_check_input = ttk.Entry(
    pwned_check_frame, 
    textvariable=inputted_password, 
    width=45)

pwned_check_input.grid(column=0, row=1, padx="15", pady="15")

pwned_check_input = ttk.Button(pwned_check_frame, text="Check")
pwned_check_input.grid(column=1, row=1, padx="15", pady="15")


def check_password(inputted_password):
    if pwned_check(inputted_password) == True:
        is_secure_message.set(inputted_password + " has not been in a data breach")
    else:
        is_secure_message.set(inputted_password + " has been in a data breach")


pwned_check_input.config(
    command=lambda: check_password(check_password(inputted_password.get())))
 
is_secure_message = tk.StringVar()

pwned_check_text = ttk.Label(pwned_check_frame, textvariable=is_secure_message)
pwned_check_text.grid(column=0, row=2, padx="15", pady="15", columnspan=2)

########################

use_pwned_check = tk.IntVar()
use_pwned_check.set(0)

use_pwned_check_box = ttk.Checkbutton(
    root, 
    text="Auto check if password is in data breach", 
    variable=use_pwned_check, 
    onvalue=1, 
    offvalue=0)

use_pwned_check_box.grid(column=3, row=4, padx="15", pady="15", columnspan=3)

# Configure the different styles
root.style = ttk.Style(root)

root.style.configure(
    "Heading.TLabel", 
    font=("Open Sans", 30), 
    background="#DBF3FA")

root.style.configure(
    "Password_Box.TLabel", 
    font=("Open Sans", 15), 
    borderwidth=2, 
    relief="flat", 
    background="#DBF3FA")

root.style.configure(
    "TButton", 
    font=("Open Sans", 15), 
    background="#DBF3FA")

root.style.configure(
    "TLabel", 
    font=("Open Sans", 15), 
    background="#DBF3FA")

root.style.configure(
    "TEntry", 
    font=("Open Sans", 15), 
    background="#DBF3FA", 
    width="30")

root.style.configure(
    "TCheckbutton", 
    font=("Open Sans", 15), 
    background="#DBF3FA")

root.style.configure(
    "TFrame", 
    background="#DBF3FA")

# Generate sample passwords
show_random_password(
    length.get(), 
    include_uppercase.get(), 
    include_numbers.get(), 
    include_symbols.get())

show_memorable_password(
    word_number.get(), 
    include_uppercase.get(), 
    include_numbers.get(), 
    include_symbols.get(), 
    uppercase_position.get(), 
    numbers_position.get(), 
    symbols_position.get())

# Start
root.mainloop()
