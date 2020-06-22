import generatorCore as generateCore
import tkinter as tk

import sys, os
def resource_path(relative_path): # function from https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

height = 300
width = 500

black = "#000000"
grey = "#262626"
green = "#89D330"
white = "#D9D9D9"

root = tk.Tk()
root.title('Password generator by mmble')
root.iconbitmap(resource_path('./icon.ico'))

def generate():
  options = (8*lc.get() + 1*uc.get() + 2*sp.get() + 4*dg.get())
  entry.delete(0, tk.END)
  if options > 0:
    entry.insert(0, generateCore.generateRandomCharacters(8, options))
  else:
    entry.insert(0, "Choose any type.")

canvas = tk.Canvas(root, height=height, width=width)
frame = tk.Frame(root, bg=black)
items = tk.Frame(frame)
title = tk.Label(items, text="Password generator by mmble", bg=black, fg=green, font=("Roboto", 16))
content = tk.Frame(items, bg=black)
entry = tk.Entry(content, bg=grey, fg=white, border=0, font=("Consolas", 34), justify='center')
button = tk.Button(content, text="Generate", bg=green, fg=grey, border=0, font=("Roboto", 22), command=generate)
types = tk.Frame(content, bg=black)

canvas.pack()
frame.place(relwidth=1, relheight=1)
items.place(x=25, y=25, relheight=1, relwidth=1, height=-50, width=-50)
title.place(relheight=0.12, relwidth=1)
content.place(rely=0.12, relheight=0.88, relwidth=1)
entry.place(relheight=0.25, relwidth=1)
button.place(rely=0.3, relheight=0.25, relwidth=1)
types.place(rely=0.6, relheight=0.4, relwidth=1)

lc = tk.IntVar()
uc = tk.IntVar()
sp = tk.IntVar()
dg = tk.IntVar()

lowercase = tk.Checkbutton(types, text="lowercase", bg=grey, fg=green, font=("Roboto", 12), variable=lc)
uppercase = tk.Checkbutton(types, text="uppercase", bg=grey, fg=green, font=("Roboto", 12), variable=uc)
special = tk.Checkbutton(types, text="special", bg=grey, fg=green, font=("Roboto", 12), variable=sp)
digits = tk.Checkbutton(types, text="digits", bg=grey, fg=green, font=("Roboto", 12), variable=dg)

lowercase.place(relx=0, rely=0, relheight=0.45, relwidth=0.49)
uppercase.place(relx=0.51, rely=0, relheight=0.45, relwidth=0.49)
special.place(relx=0, rely=0.55, relheight=0.45, relwidth=0.49)
digits.place(relx=0.51, rely=0.55, relheight=0.45, relwidth=0.49)

root.mainloop()