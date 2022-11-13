#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import tkinter module
import tkinter as tk      
 
# Following will import tkinter.ttk module and
# automatically override all the widgets
# which are present in tkinter module.
import tkinter.ttk as ttk
 
# Create Object
root = tk.Tk()
 
# Initialize tkinter window with dimensions 100x100            
root.geometry('100x100')    
 
btn = ttk.Button(root, text = 'Click me !',
                command = root.destroy)
 
# Set the position of button on the top of window
btn.pack(side = 'top')    
 
root.mainloop()

