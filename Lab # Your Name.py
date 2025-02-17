# Othman
# EET321
# 01
# Homework 1

import subprocess
import sys
from tkinter.constants import VERTICAL


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pyvisa")

# Import libraries.
import pyvisa

rm = pyvisa.ResourceManager()

#Find power supply address
try:
    Powersupply = [a for a in rm.list_resources() if 'SPD' in a]
    supply = rm.open_resource(Powersupply[0])
except IndexError:
    print("PowerSupply not connected or powered on")

#Find DMM address
try:
    Digital = [b for b in rm.list_resources() if 'SDM' in b]
    dmm = rm.open_resource(Digital[0])
except IndexError:
    print("Digital MultiMeter not connected or powered on")

#Find Osilly address
try:
    OSilly = [c for c in rm.list_resources() if 'SDS' in c]
    oscope = rm.open_resource(OSilly[0])
except IndexError:
    print("Oscilloscope not connected or powered on")

#Find Function  address
try:
    Fuci = [d for d in rm.list_resources() if 'SDG' in d]
    fungen = rm.open_resource(Fuci[0])
except IndexError:
    print("Function Generator not connected or powered on")


import tkinter as tk
from tkinter import messagebox, filedialog
import os
import random
install("pillow")
import PIL
from PIL import Image, ImageTk  # For handling image display
def show_random_image():
    """
    Opens a file dialog for the user to select a folder containing images.
    Picks a random image from the folder and displays it in the GUI.
    """
    folder = filedialog.askdirectory(title="Select a Folder with Images")  # Ask user to select a folder
    if folder:
        images = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if images:
            random_image = random.choice(images)  # Choose a random image
            image_path = os.path.join(folder, random_image)  # Get full path
            display_image(image_path)  # Display the selected image
        else:
            messagebox.showwarning("No Images", "No images found in the selected folder!")  # Warn if no images found


def display_image(image_path):
    """
    Opens and resizes an image, then displays it in the GUI.
    """
    img = Image.open(image_path)
    img = img.resize((500, 500))  # Resize image for display
    img = ImageTk.PhotoImage(img)  # Convert image for Tkinter display

    image_label.config(image=img)  # Update the label with the new image
    image_label.image = img  # Keep a reference to avoid garbage collection


def insult():
    """
    Handles user input. If they enter "Star Wars", it triggers the random image display.
    Otherwise, it insults their taste.
    """
    favorite = entry.get().strip()  # Get user input and remove extra spaces
    if favorite.lower() == "star wars":
        show_random_image()  # Show a random image if they enter "Star Wars"
    elif favorite:
        messagebox.showinfo("Terrible Taste Alert",
                            f"Why on Earth would anyone like {favorite}? You have horrible taste.")  # Display insult message
    else:
        messagebox.showwarning("Input Needed", "Please enter something!")  # Warn if input is empty


def perform_calculations():
    """
    Takes two user-inputted numbers and performs basic arithmetic operations.
    Displays the results in the GUI.
    """
    try:
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())

        # Performing calculations
        results_text.set(
            f"{num1} + {num2} = {num1 + num2}\n"
            f"{num1} - {num2} = {num1 - num2}\n"
            f"{num2} - {num1} = {num2 - num1}\n"
            f"{num1} * {num2} = {num1 * num2}\n"
            f"{num1} / {num2} = {num1 / num2:.2f}"  # Formatting division result to 2 decimal places
        )
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid integers!")


def calculate_gpa():
    """
    Asks the user for their name and their grades in seven classes.
    Calculates and displays the average grade.
    """
    try:
        name = name_entry.get().strip()
        grades = [int(grade_entry[i].get()) for i in range(7)]  # Get grades from input fields
        average_grade = sum(grades) / len(grades)  # Calculate GPA

        gpa_text.set(f"Your current average grade is {average_grade:.2f}, {name}.")  # Display result
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid grades (numbers only)!")


def print_house():
    """
    Displays an ASCII house inside a message box.
    """
    house = """
       /\\
      /  \\
     /____\\
    |      |
    |  []  |
    |______|
    """
    messagebox.showinfo("House Drawing", house)


# Create the main window
root = tk.Tk()
root.title("Mom GUI")  # Set window title
root.attributes('-fullscreen', True)  # Set to full-screen mode

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient=VERTICAL)
scrollbar.pack(fill=tk.Y,side=tk.LEFT)


def exit_fullscreen(event=None):
    """
    Exits full-screen mode when the Escape key is pressed.
    """
    root.attributes('-fullscreen', False)


# Bind the Escape key to exit full screen
root.bind("<Escape>", exit_fullscreen)

# --- Section 1: Favorite Movie/Band Entry ---
label = tk.Label(root, text="Enter your favorite movie, song, or band:", font=("Arial", 20))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18), width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", font=("Arial", 18), command=insult)
button.pack(pady=10)

#Escape
label = tk.Label(root, text="Use the escape button to exit full screen", font=("Arial", 10))
label.pack(pady=10)

# --- Section 2: Calculator UI ---
calc_label = tk.Label(root, text="Enter two numbers for calculations:", font=("Arial", 20))
calc_label.pack(pady=10)

# Entry fields for numbers
num1_entry = tk.Entry(root, font=("Arial", 18), width=10)
num1_entry.pack(pady=5)
num2_entry = tk.Entry(root, font=("Arial", 18), width=10)
num2_entry.pack(pady=5)

# Calculation button
calc_button = tk.Button(root, text="Calculate", font=("Arial", 18), command=perform_calculations)
calc_button.pack(pady=10)

# Label to display calculation results
results_text = tk.StringVar()
results_label = tk.Label(root, textvariable=results_text, font=("Arial", 18), justify="left")
results_label.pack(pady=10)

# --- Section 3: GPA Calculator ---
gpa_label = tk.Label(root, text="Enter your first name and grades for 7 classes:", font=("Arial", 20))
gpa_label.pack(pady=10)

# Name Entry Field
name_entry = tk.Entry(root, font=("Arial", 18), width=30)
name_entry.pack(pady=5)

# Grade Entry Fields (7 Classes)
grade_entry = []
for i in range(7):
    grade_label = tk.Label(root, text=f"Class {i + 1} Grade:", font=("Arial", 16))
    grade_label.pack()
    entry_field = tk.Entry(root, font=("Arial", 16), width=10)
    entry_field.pack(pady=2)
    grade_entry.append(entry_field)

# GPA Calculation Button
gpa_button = tk.Button(root, text="Calculate GPA", font=("Arial", 18), command=calculate_gpa)
gpa_button.pack(pady=10)

# GPA Result Label
gpa_text = tk.StringVar()
gpa_label_result = tk.Label(root, textvariable=gpa_text, font=("Arial", 18), justify="center")
gpa_label_result.pack(pady=10)

# --- Section 4: House Print Button ---
house_button = tk.Button(root, text="Print House", font=("Arial", 18), command=print_house)
house_button.pack(pady=10)

# --- Section 5: Image Display (Initially Empty) ---
image_label = tk.Label(root)
image_label.pack(pady=20)



# Run the GUI loop
root.mainloop()


