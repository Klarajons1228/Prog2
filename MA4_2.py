#!/usr/bin/env python3.9

# from person import Person
# 
# def main():
# 	f = Person(5)
# 	print(f.get())
# 	f.set(7)
# 	print(f.get())
# 
# if __name__ == '__main__':
# 	main()

# import tkinter as tk
# 
# border_effects = {   "flat": tk.FLAT,   "sunken": tk.SUNKEN,   "raised": tk.RAISED,   "groove": tk.GROOVE,   "ridge": tk.RIDGE,}
# 
# window = tk.Tk()
# # for relief_name, relief in border_effects.items():
# #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
# #     frame.pack(side=tk.LEFT)
# #     label = tk.Label(master=frame, text=relief_name)
# #     label.pack()
# # frame = tk.Frame(master=window, width=150, height=150, bg="red")
# # frame.pack(fill=tk.BOTH,expand = True)
# 
# label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()
# button = tk.Button(text="Click me!",width=25,height=5,bg="blue",fg="black",)
# button.pack()
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
# label.pack()
# window.mainloop()

from tkinter import *
from tkinter.ttk import *
import random
 
class GFG:
    def __init__(self, master = None):
        self.master = master
         
        # to take care movement in x direction
        self.x_pos = 1
        # to take care movement in y direction
        self.y_pos = 0
 
        # canvas object to create shape
        self.canvas = Canvas(master)
        # creating rectangle
        self.objects = []
        for i in range(5):
            ob = self.canvas.create_oval(5, 5, 25, 25, fill = "black")
            self.objects.append(ob)
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()
     
    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        for ob in self.objects:
            x = random.randint(-10,20)
            y = random.randint(-10,20)
            self.canvas.move(ob, x, y)
 
        self.canvas.after(100, self.movement)
 
if __name__ == "__main__":
 
    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()
    gfg = GFG(master)
 
    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
     
    # Infinite loop breaks only by interrupt
    mainloop()