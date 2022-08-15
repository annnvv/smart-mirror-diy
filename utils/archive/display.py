from datetime import datetime, time
from tkinter import Tk, Label, Frame, NW, NE, S, W, SW, SE, END
import tkinter.font as tkFont
from tkinter.ttk import Treeview, Style
from PIL import ImageTk, Image

from clock import Clock
from weather import Weather
from train import Wmata

##TODO: (HIGH priority)implement after method to refresh the GUI with update data

# from utils.text import displayOptions
##TODO: (low priority)implement displayOptions (have displayWindow inheret this class)

# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop

root = Tk()
root.title("")
root.configure(background="black")
# root.wm_attributes("-fullscreen", "True") ##av.note really difficult to close (have to go to task manager); probably will use this in final version of gui
root.state("zoomed")  # start app with maximized display

bg_color = "black"
text_color = "white"

pad30 = 30

font_name = "Lucida Grande"  ##Helvetica
fontStyleLarge = tkFont.Font(family=font_name, size=32)
fontStyleMedium = tkFont.Font(family=font_name, size=24)
fontStyleSmall = tkFont.Font(family=font_name, size=16)

##Frames
## Numbered left to right and top to bottom
## odd frames will have content, even frames will be empty)

##TODO: (low priority)implement logic if there are more than one screen; this code pulls from main screen
frame_height = root.winfo_screenheight() / 3
frame_width = root.winfo_screenwidth() / 3

frame1 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame1.grid(row=0, column=0)
## TODO (low priority) figure out difference between pack_propagate and grid_propagate
frame1.pack_propagate(False)

frame2 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame2.grid(row=0, column=1)
frame2.pack_propagate(False)

frame3 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame3.grid(row=0, column=2)
frame3.pack_propagate(False)

frame4 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame4.grid(row=1, column=0)

frame5 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame5.grid(row=1, column=1)

frame6 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame6.grid(row=1, column=2)

frame7 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame7.grid(row=2, column=0, sticky=SW, padx=(pad30, 0))
frame7.pack_propagate(True)

frame8 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame8.grid(row=2, column=1)

frame9 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
frame9.grid(row=2, column=2)
frame9.pack_propagate(False)

## Date and Time (Top Left)
clock = Clock()
clock.get_clock_info()

dow = Label(frame1, text=clock.dow, font=fontStyleLarge, bg=bg_color, fg=text_color,)
dow.pack(pady=(pad30, 0), padx=(pad30, 0), anchor=NW)

date = Label(frame1, text=clock.date, font=fontStyleMedium, bg=bg_color, fg=text_color,)
date.pack(padx=(pad30, 0), anchor=NW)

time = Label(frame1, text=clock.time, font=fontStyleLarge, bg=bg_color, fg=text_color,)
time.pack(padx=(pad30, 0), anchor=NW)
time.after(2000, clock.get_clock_info)

## Greeting (Center)
##TODO:(low priority)implement conditional greeting (Good Morning, Good Afternoon, Good Evening)
greeting = Label(
    frame2, text="Hello, Anna!", font=fontStyleLarge, bg=bg_color, fg=text_color
)
greeting.pack(pady=pad30)

## Weather (Top Right)
weather_data = Weather()
weather_data.get_weather()

degree_sign = "\N{DEGREE SIGN}"
current_temp = Label(
    frame3,
    text=weather_data.temp + degree_sign,
    font=fontStyleLarge,
    bg=bg_color,
    fg=text_color,
)
current_temp.pack(pady=(pad30, 0), padx=pad30, anchor=NE)

feels_like = Label(
    frame3,
    text="Feels like " + weather_data.feels_like + degree_sign,
    font=fontStyleSmall,
    bg=bg_color,
    fg=text_color,
)
feels_like.pack(padx=pad30, anchor=NE)

daily_max_min = Label(
    frame3,
    text=weather_data.temp_max
    + degree_sign
    + " | "
    + weather_data.temp_min
    + degree_sign,
    font=fontStyleSmall,
    bg=bg_color,
    fg=text_color,
)
daily_max_min.pack(padx=pad30, anchor=NE)

desc = Label(
    frame3,
    text=weather_data.weather_desc,
    font=fontStyleMedium,
    bg=bg_color,
    fg=text_color,
)
desc.pack(padx=pad30, anchor=NE)

##TODO: (HIGH priority)need to implement a .remove method for the label so that each image doesn't get stacked on top
weather_img = ImageTk.PhotoImage(Image.open(weather_data.img_path).resize((95, 95)))
weather_img_lbl = Label(frame3, image=weather_img, borderwidth=0)
weather_img_lbl.pack(padx=pad30, anchor=NE)


sun = Label(
    frame8,
    text="Rise " + weather_data.sunrise + " | Set  " + weather_data.sunset,
    font=fontStyleSmall,
    bg=bg_color,
    fg=text_color,
)
sun.pack(anchor=S)


## Metro (Bottom Left)
train = Wmata()
train.get_next_train()

##TODO: (medium priority)change the background and foreground color of rows!
style = Style()
style.theme_use("classic")
style.configure(
    "Treeview",
    background=bg_color,
    fieldbackground=bg_color,
    foreground=text_color,
    rowheight=40,
    font=fontStyleSmall,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)

style.configure(
    "Treeview.Heading",
    font=fontStyleMedium,
    anchor=W,
    background=bg_color,
    foreground=text_color,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)

columns = ("Line", "Destination", "Min")

tree = Treeview(frame7, columns=columns, show="headings")

tree.column("Line", width=80, anchor=W)
tree.column("Destination", width=200, anchor=W)
tree.column("Min", width=80, anchor=W)

tree.heading("Line", text="Line", anchor=W)
tree.heading("Destination", text="Destination", anchor=W)
tree.heading("Min", text="Min", anchor=W)

tree.tag_configure("row", background="black")


if train.train_info:
    for row in train.train_info:
        tree.insert("", END, values=row, tags="row")

tree.pack(anchor=S)

## Bus (Bottom Right)

root.mainloop()
