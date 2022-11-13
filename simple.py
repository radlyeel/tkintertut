#!/usr/bin/env python3
import tkinter as tk


# create root window
root = tk.Tk()						

# frame inside root window
frame = tk.Frame(root)				

# geometry method
frame.pack()						

# button inside frame which is
# inside root
button = tk.Button(frame, text ='Geek')
button.pack()						

# Tkinter event loop
root.mainloop()					

