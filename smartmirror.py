# smartmirror.py

from tkinter import Tk
from utils.display_class import Display

root = Tk()
root.title("")
root.configure(background="black")
# root.wm_attributes("-fullscreen", "True") ##av.note really difficult to close (have to go to task manager); probably will use this in final version of gui
root.state("zoomed")  # start app with maximized display

app = Display(master=root)

root.mainloop()
