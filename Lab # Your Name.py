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
root.title("Mom GUI")  # Set window title
root.attributes('-fullscreen', True)  # Set to full-screen mode
