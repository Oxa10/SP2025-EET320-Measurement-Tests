# Othman
# EET321
# 01
# Homework 2

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pyvisa")

# Import tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Homework 2")  # Set window title
root.attributes('-fullscreen', True)  # Set to full-screen mode


def exit_fullscreen(event=None):
    """
    Exits full-screen mode when the Escape key is pressed.
    """
    root.attributes('-fullscreen', False)

# Bind the Escape key to exit full-screen mode
root.bind("<Escape>", exit_fullscreen)

# -- Problem 1 -- Scaring the User
def Creepy():
    """
    Displays a creepy message in a new window.
    """
    creepy_window = tk.Toplevel(root)  # Create a new top-level window
    creepy_window.title("Warning!")

    label = tk.Label(creepy_window, text='I am "watching" you...', font=("Arial", 16), fg="red")
    label.pack(pady=20)

    button = tk.Button(creepy_window, text="Close", command=creepy_window.destroy)
    button.pack()

# -- Problem 2 -- Guess my Song
def Song():
    """
    Displays a Song message in a new window.
    """
    song_window = tk.Toplevel(root)  # Create a new top-level window
    song_window.title("Can you guees it!")

    label = tk.Label(song_window, text='''اضحك (اضحك، اضحك، اضحك)
اضحك خلي البسمة تنور قلبك
خلي الفرحة تضوّي دربك
ما في شي في الدنيا يسوى تزعّل روحك، اضحك''', font=("Arial", 16), fg="red")
    label.pack(pady=20)

    button = tk.Button(song_window, text="Close", command=song_window.destroy)
    button.pack()

# -- Problem 3 -- Text stuff
def LeamKneeson():
    """
    solves problem 3 normallay because IDK how to do this in tkinter.
    """
    # Assigning a famous movie quote to a variable
    the_guy_from_NextOfKin_and_Batman = "But if you don't, I will look for you, I will find you, and I will kill you."

    # Printing a message about the number of characters in the string
    print('The Number of characters in this string')

    # Printing the length of the string
    print(len(the_guy_from_NextOfKin_and_Batman))

    # Printing a message indicating which character will be displayed
    print('this is the 14th character')

    # Printing the 14th character (index 13 since Python uses zero-based indexing)
    print(the_guy_from_NextOfKin_and_Batman[13])

    # Extracting a substring from the 20th to the 49th character
    i_know_Why_This_part_IS_IMPORTANT_BUT_I_am_so_bored = the_guy_from_NextOfKin_and_Batman[20:49]

    # Printing a message describing the extracted substring
    print('this is the 20th to the 49th characters')

    # Printing the extracted substring
    print(i_know_Why_This_part_IS_IMPORTANT_BUT_I_am_so_bored)

    # Extracting the last 4 characters of the string
    i_shouldnt_Have_Procrastinated_this_until_10PM = the_guy_from_NextOfKin_and_Batman[-4:]

    # Printing a message describing the last 4 characters
    print('this is the last 4')

    # Printing the last 4 characters of the string
    print(i_shouldnt_Have_Procrastinated_this_until_10PM)

# -- Problem 4 -- Collecting Stuff
from tkinter import simpledialog
def Collecting_Stuff():
    #will ask induvually please press button multipale times to make work correctly
    first_name = simpledialog.askstring("Input", "Enter your first name:")

    last_name = simpledialog.askstring("Input", "Enter your last name:")

    birthday = simpledialog.askstring("Input", "Enter your birthday:")

    hometown = simpledialog.askstring("Input", "Enter your hometown:")

    favorite_number = simpledialog.askstring("Input", "Enter your favorite number:")

    info = first_name + "," + last_name + "," + birthday + "," + hometown + "," + favorite_number

    label_result.config(text=f"Stored Info: {info}")

# -- Problem 5 -- Mad Lib

from tkinter import messagebox

def generate_madlib():
    words = []
    prompts = ["adjective", "Hand Held Object", "verb", "number", "place", "animal", "80s verb", "food", "emotion", "celebrity"]

    popup = tk.Toplevel(root)
    popup.title("Enter Words")
    popup.geometry("300x400")

    entries = []
    for i, prompt in enumerate(prompts):
        tk.Label(popup, text=f"Enter a {prompt}:").pack()
        entry = tk.Entry(popup)
        entry.pack()
        entries.append(entry)

    def submit():
        for entry in entries:
            words.append(entry.get())
        popup.destroy()
        show_madlib(words)

    tk.Button(popup, text="Submit", command=submit).pack()


def show_madlib(words):
    story = (f"""I Saw a {words[0]} dude. So after seeing him I reached for my {words[1]} and {words[2]} 
             him {words[3]} times. Then, I went to {words[4]} and saw a {words[5]} person.
             It was so {words[6]}! Later, I found {words[7]} that made me feel {words[8]}s also for some reason {words[9]} just lying around.""")


    messagebox.showinfo("Your Mad Lib", story)


# Create a button to trigger my functions
creepy_button = tk.Button(root, text="Click if you dare!", command=Creepy, font=("Arial", 20))
creepy_button.pack(pady=50)

song_button = tk.Button(root, text="Guess this song", command=Song, font=("Arial", 20))
song_button.pack(pady=50)

LeamKneeson()

# Create labels and entry fields
labels = ["First Name:", "Last Name:", "Birthday:", "Hometown:", "Favorite Number:"]
entries = []

# Create submit button
submit_button = tk.Button(root, text="Submit", command=Collecting_Stuff)
submit_button.pack(pady=5)

# Create result label
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

#MAking me go "Mad"
tk.Label(root, text="Mad Lib Generator", font=("Arial", 14)).pack(pady=20)
tk.Button(root, text="Generate Mad Lib", command=generate_madlib).pack()

# Run the GUI loop
root.mainloop()
