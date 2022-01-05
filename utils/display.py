from datetime import datetime
from tkinter import Tk, Label, Frame, NW, NE, SW, SE
import tkinter.font as tkFont
from PIL import ImageTk, Image

# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop


class displayWindow:

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
    fontStyleSmall = tkFont.Font(family=font_name, size=12)

    ##Frames
    ## Numbered left to right and top to bottom
    ## odd frames will have content, even frames will be empty)

    frame_height = root.winfo_screenheight() / 3
    frame_width = root.winfo_screenwidth() / 3

    frame1 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
    frame1.grid(row=0, column=0)
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
    frame7.grid(row=2, column=0)
    frame7.pack_propagate(False)

    frame8 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
    frame8.grid(row=2, column=1)

    frame9 = Frame(root, bg=bg_color, height=frame_height, width=frame_width)
    frame9.grid(row=2, column=2)
    frame9.pack_propagate(False)

    ## Date and Time (Top Left)
    dow = Label(
        frame1,
        text=datetime.today().strftime("%A"),
        font=fontStyleLarge,
        bg=bg_color,
        fg=text_color,
    )
    dow.pack(pady=(pad30, 0), padx=(pad30, 0), anchor=NW)

    date = Label(
        frame1,
        text=datetime.today().strftime("%B %d, %Y"),
        font=fontStyleMedium,
        bg=bg_color,
        fg=text_color,
    )
    date.pack(padx=(pad30, 0), anchor=NW)

    time = Label(
        frame1,
        text=datetime.now().strftime("%H:%M"),
        font=fontStyleMedium,
        bg=bg_color,
        fg=text_color,
    )
    time.pack(padx=(pad30, 0), anchor=NW)

    ## Weather (Top Right)
    degree_sign = "\N{DEGREE SIGN}"
    current_temp = Label(
        frame3, text="48" + degree_sign, font=fontStyleLarge, bg=bg_color, fg=text_color
    )
    current_temp.pack(pady=(pad30, 0), padx=pad30, anchor=NE)

    weather_img = ImageTk.PhotoImage(Image.open("imgs/Sun.png").resize((95, 95)))
    weather_img_lbl = Label(frame3, image=weather_img, borderwidth=0)
    weather_img_lbl.pack(padx=pad30, anchor=NE)

    feels_like = Label(
        frame3,
        text="Feels like 46" + degree_sign,
        font=fontStyleSmall,
        bg=bg_color,
        fg=text_color,
    )
    feels_like.pack(padx=pad30, anchor=NE)

    daily_max_min = Label(
        frame3,
        text="56" + degree_sign + " | " + "40" + degree_sign,
        font=fontStyleSmall,
        bg=bg_color,
        fg=text_color,
    )
    daily_max_min.pack(padx=pad30, anchor=NE)

    ## Greeting (Center)
    greeting = Label(
        frame2, text="Hello, Anna!", font=fontStyleLarge, bg=bg_color, fg=text_color
    )
    greeting.pack(pady=pad30)

    ## Metro (Bottom Left)
    train_lbl = Label(
        frame7,
        text="Line    Destination    Min",
        font=fontStyleMedium,
        bg=bg_color,
        fg=text_color,
    )
    train_lbl.pack(pady=(pad30, 0), padx=(pad30, 0), anchor=SW)
    train = Label(
        frame7,
        text="BL        Franconia         5 ",
        font=tkFont.Font(family=font_name, size=20),
        bg=bg_color,
        fg=text_color,
    )
    train.pack(padx=(pad30, 0), anchor=SW)

    ## Bus (Bottom Right)

    # root.mainloop()
