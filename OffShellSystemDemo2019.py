#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import random
import string
import os
import webbrowser

def web1():
    os.system('lynx offshellsystem.blogspot.com')
    
    root.mainloop()


def consola():
    root = Tk()
    root.config(bg="black")
    root.geometry("750x650")
    root.resizable(width=False, height=False)
    Label(root, text="OffShell System||Console", font=("URW Chancery L", 16), background='black', fg="red").pack()


    termf = Frame(root, height=600, width=600) 

    termf.pack(fill=BOTH, expand=1) 
    wid = termf.winfo_id() 
    os.system('xterm -into %d -geometry 600x600 -sb &' % wid)

    root.title("*** OffShell System | Custom Console ***")
    root.config(bg="black")
    root.geometry("750x650")
    root.mainloop()

def exit():
    root.quit()

print ('Wellcome User.')
os.system('apt install lynx')
print ('--PROCESS COMPLETE--')
print ('--CONNECTING--')

root = Tk()

root.title("OffShell*System")
root.config(bg="black")
root.geometry("350x350")
root.resizable(width=False, height=False)

Label(root, text="OffShell System\nDemo Tools", font=("URW Chancery L", 24), background='black', fg="red").pack()
Label(root, text="", font=("URW Chancery L", 24), background='black', fg="red").pack()

Button(root, text="Console", command=consola, font=("URW Chancery L", 16), background='black', fg="red").pack()
Label(root, text="Custom console", font=("URW Chancery L", 16), background='black', fg="purple").pack()

Label(root, text="||", font=("URW Chancery L", 20), background='black', fg="red").pack()

Button(root, text="Browser", command=web1, font=("URW Chancery L", 16), background='black', fg="red").pack()
Label(root, text="Tecnopat browser", font=("URW Chancery L", 16), background='black', fg="purple").pack()

Button(root, text="Exit", command=exit, font=("URW Chancery L", 8), background='black', fg="red").pack(side=RIGHT)

root.mainloop()
