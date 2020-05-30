
from tkinter import messagebox
from tkinter import *
import pyautogui
import time
from PIL import *


positions = []
ind = 0
def mine():
    if len(positions) < 2:
        messagebox.showinfo("Add Positions","Need at least 2 positions to mine.")
    else:
        move_helper()

def move_helper():
    global ind,positions
    if ind in range(0,len(positions)):
        pos = positions[ind]
        pyautogui.leftClick(*pos)
        root.after(2000,mine_helper)

def mine_helper():
    global ind,positions
    pyautogui.typewrite('d')
    ind = (ind + 1) % len(positions)
    root.after(12000,move_helper)

def end():
    root.destroy()

def add_position():
    time.sleep(5)
    pos = pyautogui.position()
    positions.append(pos)
    messagebox.showinfo("Position Added", f"{pos} added to list")

def helper():
    messagebox.showinfo("Help","To Add Position click on an open area in Mine Cave then wait 5 seconds.")


root = Tk()
root.title("CPR AutoMiner")
root.geometry("240x100")
root.resizable(width=False, height=False)
topFrame = Frame(root)
how_to = Button(root,text="Help",command = helper)
adding_position = Button(root,text="Add Position",command=add_position)
auto_mine = Button(root,text="Mine",command=mine)
end_mine = Button(root,text="End",command=end)
adding_position.place(x=75,y=25)
auto_mine.place(x=100,y=50)
end_mine.place(x=103,y=75)
how_to.place(x=10,y=5)
root.mainloop()
