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
    root.geometry("800x600")
    root.resizable(width=False, height=False)

    Label(root, text="OffShell System", font=("URW Chancery L", 14), background='black', fg="red").pack()


    termf = Frame(root, height=750, width=250) 

    termf.pack(fill=BOTH, expand=0) 
    wid = termf.winfo_id() 
    os.system('xterm -into %d -geometry 300x300 -sb &' % wid)
    Button(root, text="Popular repositories ", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="Exit", command=exit, font=("URW Chancery L", 10), background='black', fg="red").pack(side=RIGHT)
    Button(root, text="Diccionary", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="Scripts", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="Admin", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="Protocol", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="Updates", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    Button(root, text="DataBase", font=("URW Chancery L", 10), background='black', fg="red").pack(side=LEFT)
    

    root.title("*** OffShell System | Custom Console ***")
    root.config(bg="black")
    root.geometry("800x800")
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
root.geometry("350x450")
root.resizable(width=False, height=False)

frame1=Frame()

frame1.pack(fill="x")

Label(frame1, text="OffShell System", bg="purple", fg="red", font=("Fantasque Sans Mono", 23)).grid(row=2, column=4)

frame1.config(bg="purple")
frame1.config(width="350", height="350")
frame1.config(bd=30)
frame1.config(relief="sunken")


Label(root, text="", font=("URW Chancery L", 24), background='black', fg="red").pack()

Button(root, text="Console", command=consola, font=("URW Chancery L", 16), background='black', fg="red").pack()
Label(root, text="Custom console", font=("URW Chancery L", 16), background='black', fg="white").pack()

Label(root, text="||", font=("URW Chancery L", 20), background='black', fg="red").pack()

Button(root, text="Browser", command=web1, font=("URW Chancery L", 16), background='black', fg="red").pack()
Label(root, text="Tecnopat browser", font=("URW Chancery L", 16), background='black', fg="white").pack()

Label(root, text="OffShell System\nDemo Tools", font=("URW Chancery L", 24), background='black', fg="red").pack()

Button(root, text="Exit", command=exit, font=("URW Chancery L", 8), background='black', fg="red").pack()

root.mainloop()
