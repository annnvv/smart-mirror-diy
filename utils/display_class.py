from datetime import datetime
import tkinter as tk
from tkinter import Label, Frame, StringVar, NW, NE, S, W, SW, SE, END, CENTER
import tkinter.font as tkFont
from tkinter.ttk import Treeview, Style
from PIL import ImageTk, Image

from threading import Thread

import requests
import json

from read_yaml import configData

cfd = configData()

## Frames - Numbered left to right and top to bottom
class Display(tk.Frame):
    def __init__(self, master):
        bg_color = "black"
        text_color = "white"

        pad30 = 30

        font_name = "Lucida Grande"  ##Helvetica
        fontStyleLarge = tkFont.Font(family=font_name, size=32)
        fontStyleMedium = tkFont.Font(family=font_name, size=24)
        fontStyleSmall = tkFont.Font(family=font_name, size=16)

        ##TODO: (medium priority)implement logic if there are more than one screen; this code pulls from main screen
        frame_height = master.winfo_screenheight() / 3
        frame_width = master.winfo_screenwidth() / 3

        tk.Frame.__init__(self, master)

        frame1 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame2 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame3 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame4 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame5 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame6 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame7 = Frame(
            master,
            bg=bg_color,
            height=frame_height,
            width=frame_width,
            background=bg_color,
            relief="flat",
        )
        frame8 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame9 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)

        frame1.grid(row=0, column=0)
        frame2.grid(row=0, column=1)
        frame3.grid(row=0, column=2)
        frame4.grid(row=1, column=0)
        frame5.grid(row=1, column=1)
        frame6.grid(row=1, column=2)
        frame7.grid(row=2, column=0, sticky=SW, padx=(pad30, 0))
        frame8.grid(row=2, column=1)
        frame9.grid(row=2, column=2)

        ## TODO (medium priority) figure out difference between pack_propagate and grid_propagate
        frame1.pack_propagate(False)
        frame2.pack_propagate(False)
        frame3.pack_propagate(False)
        frame7.pack_propagate(True)
        frame9.pack_propagate(False)

        ## Date and Time (Top Left Frame)
        self.dow_var = StringVar()
        dow_lbl = Label(
            frame1,
            textvariable=self.dow_var,
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        dow_lbl.pack(anchor=NW)  # grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.date_var = StringVar()
        date_lbl = Label(
            frame1,
            textvariable=self.date_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        date_lbl.pack(anchor=NW)  # grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.time_var = StringVar()
        time_lbl = Label(
            frame1,
            textvariable=self.time_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        time_lbl.pack(anchor=NW)  # .grid(row=2, column=0, padx=5, pady=5, sticky=W)

        Thread(target=self.get_date_time()).start()

        ## Greeting (Top Middle Frame)
        ##TODO:(low priority)implement conditional greeting (Good Morning, Good Afternoon, Good Evening)
        greeting_lbl = Label(
            frame2,
            text="Hello, Anna!",
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        greeting_lbl.pack(pady=pad30)

        # ## Weather (Top Right Frame)
        self.temp_var = StringVar()
        current_temp_lbl = Label(
            frame3,
            textvariable=self.temp_var,
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        current_temp_lbl.pack(pady=(pad30, 0), padx=pad30, anchor=NE)

        self.feels_like_var = StringVar()
        feels_like_lbl = Label(
            frame3,
            textvariable=self.feels_like_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        feels_like_lbl.pack(padx=pad30, anchor=NE)

        self.temp_max_min_var = StringVar()
        daily_max_min_lbl = Label(
            frame3,
            textvariable=self.temp_max_min_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        daily_max_min_lbl.pack(padx=pad30, anchor=NE)

        self.weather_desc_var = StringVar()
        desc_lbl = Label(
            frame3,
            textvariable=self.weather_desc_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        desc_lbl.pack(padx=pad30, anchor=NE)

        # ##TODO: (HIGH priority)need to implement a .remove method for the label so that each image doesn't get stacked on top
        self.img_path_var = StringVar()
        # weather_img = ImageTk.PhotoImage(Image.open(self.img_path_var).resize((95, 95)))
        # weather_img_lbl = Label(frame3, image=weather_img, borderwidth=0)
        # weather_img_lbl.pack(padx=pad30, anchor=NE)

        self.sun_rise_set_var = StringVar()
        sun_lbl = Label(
            frame8,
            textvariable=self.sun_rise_set_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        sun_lbl.pack(anchor=S)

        Thread(target=self.get_weather(cfd))

        ## Metro (Bottom Left)
        ### self.train = Wmata(self.frame7, cfd._wmata_api_key, cfd._wmata_station_code)

        ##TODO: (in progress - medium priority)change the background and foreground color!
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
        ##TODO: remove borders
        # # style.layout(
        # #     "Treeview", [("Treeview.treearea", {"sticky": "wnes"})]
        # # )  # Remove the borders
        style.layout("Treeview", [("Treeview.field", {"border": "0"})])
        style.map("Treeview")

        style.configure(
            "Treeview.Heading",
            font=fontStyleMedium,
            anchor=W,
            background=bg_color,
            foreground=text_color,
            fieldbackground=bg_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        style.map("Treeview.Heading")

        columns = ("Line", "Destination", "Min")

        tree = Treeview(frame7, columns=columns, show="headings")

        tree.column("Line", width=80, anchor=W)
        tree.column("Destination", width=200, anchor=W)
        tree.column("Min", width=80, anchor=W)

        tree.heading("Line", text="Line", anchor=W)
        tree.heading("Destination", text="Destination", anchor=W)
        tree.heading("Min", text="Min", anchor=W)

        # self.train_info =
        # if train.train_info:
        #     for row in train.train_info:
        #         tree.insert("", END, values=row)

        tree.pack(anchor=S)

    def get_date_time(self):
        self.dow_var.set(datetime.today().strftime("%A"))
        self.date_var.set(datetime.today().strftime("%B %d, %Y"))
        self.time_var.set(datetime.now().strftime("%H:%M"))

        self.after(1000, self.get_date_time)

    def get_weather(self, config):
        ## Make GET request
        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={config._weather_zip_code}&appid={config._weather_api_key}&units=imperial"
        )

        try:
            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)
            # print(weather_obj)
        except requests.exceptions.RequestException as e:
            print("Raise error:", e)

        ## Parse data from request
        degree_sign = "\N{DEGREE SIGN}"
        self.temp_var.set(str(round(weather_obj["main"]["temp"])) + degree_sign)

        self.feels_like_var.set(
            "Feels like " + str(round(weather_obj["main"]["feels_like"])) + degree_sign
        )

        self.temp_max_min_var.set(
            "Max "
            + str(round(weather_obj["main"]["temp_max"]))
            + degree_sign
            + " | "
            + "Min "
            + str(round(weather_obj["main"]["temp_min"]))
            + degree_sign
        )

        self.weather_desc_var.set(weather_obj["weather"][0]["main"])
        # self.img_path_var.set(self.__icon_lookup[self.weather_desc.lower()])

        self.sun_rise_set_var.set(
            "Rise "
            + datetime.fromtimestamp(weather_obj["sys"]["sunrise"]).strftime("%H:%M")
            + " | "
            + "Set  "
            + datetime.fromtimestamp(weather_obj["sys"]["sunset"]).strftime("%H:%M")
        )

        self.after(900000, self.get_weather)  # 900000ms = 15 minutes

    def get_train_info(self, config):
        ## Make GET request (only when metro station is open)
        wmata_req_url = str(
            f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{config._wmata_station_code}"
        )
        headers = {
            "api_key": config._wmata_api_key,
        }

        # ##TODO2: (medium priority) limit requests only during when the train is running (note to self: this might be more appropriate in the display/GUI than here)
        try:
            r = requests.get(wmata_req_url, params=headers)
            train_obj = json.loads(r.text)

        except requests.exceptions.RequestException as e:
            print("Error:", e)

        ## Parse data from request
        ##TODO: (HIGH priority) Need to figure out how to parse this info to feed it into the table
        self.train_info = []
        if train_obj["Trains"]:
            for i in range(len(train_obj["Trains"])):
                train = [
                    [train_obj["Trains"][i]["Line"]],
                    [train_obj["Trains"][i]["Destination"]],
                    [train_obj["Trains"][i]["Min"]],
                ]
                self.train_info.append(train)
        return None


# root = tk.Tk()
# root.title("")
# root.configure(background="black")
# # root.wm_attributes("-fullscreen", "True") ##av.note really difficult to close (have to go to task manager); probably will use this in final version of gui
# root.state("zoomed")  # start app with maximized display

# app = Display(master=root)

# root.mainloop()
