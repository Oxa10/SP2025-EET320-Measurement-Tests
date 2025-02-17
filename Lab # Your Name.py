# YOUR NAME
# EET321
# SECTION NUMBER
# ASSIGNMENT NAME
# DATE
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

# -- Problem 1 -- Scaring the User
def Creepy():

# Bind the Escape key to exit full screen
root.bind("<Escape>", exit_fullscreen)

# Run the GUI loop
root.mainloop()

