from datetime import datetime
import tkinter as tk
from tkinter import Label, Frame, Canvas, StringVar, BOTH, N, E, NW, NE, S, W, SW, SE, END, CENTER
import tkinter.font as tkFont
from tkinter.ttk import Treeview, Style
from threading import Thread

import requests
from PIL import ImageTk, Image

from read_yaml import configData

cfd = configData()

## Frames - Numbered left to right and top to bottom
class Display(tk.Frame):
    def __init__(self, master):
        bg_color = "black"
        text_color = "white"

        pad30 = 30

        font_name = "Lucida Grande"  ##Helvetica
        fontStyleLarge = tkFont.Font(family=font_name, size=37)
        fontStyleMedium = tkFont.Font(family=font_name, size=28)
        fontStyleSmall = tkFont.Font(family=font_name, size=21)

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
        frame7 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame8 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)
        frame9 = Frame(master, bg=bg_color, height=frame_height, width=frame_width)

        frame1.grid(row=0, column=0, sticky = NW)
        frame2.grid(row=0, column=1)
        frame3.grid(row=0, column=2, sticky = E)
        frame4.grid(row=1, column=0, sticky = W)
        frame5.grid(row=1, column=1)
        frame6.grid(row=1, column=2, sticky = E)
        frame7.grid(row=2, column=0, sticky = SW)
        frame8.grid(row=2, column=1, stick = S)
        frame9.grid(row=2, column=2, sticky = E)

        ## Date and Time (Top Left Frame)
        self.sun_rise_set_var = StringVar()
        sun_lbl = Label(
            frame1,
            textvariable=self.sun_rise_set_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        sun_lbl.pack(anchor = W, pady=(pad30,0), padx = (10, 0))

        self.dow_var = StringVar()
        dow_lbl = Label(
            frame1,
            textvariable=self.dow_var,
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        dow_lbl.pack(anchor = W, padx = (pad30, 0))

        self.date_var = StringVar()
        date_lbl = Label(
            frame1,
            textvariable=self.date_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        date_lbl.pack(anchor = W, padx = (pad30, 0))

        self.time_var = StringVar()
        time_lbl = Label(
            frame1,
            textvariable=self.time_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        time_lbl.pack(anchor = W, padx = (pad30, 0))

        self.update_thread = Thread(target=self.get_date_time())
        self.update_thread.daemon = True
        self.update_thread.start()

        ## Greeting (Top Middle Frame)
        ##TODO:(low priority)implement conditional greeting (Good Morning, Good Afternoon, Good Evening)
        greeting_lbl = Label(
            frame2,
            text="Hello, Anna!",
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        greeting_lbl.pack()

        # ## Weather (Top Right Frame)
        self.temp_var = StringVar()
        current_temp_lbl = Label(
            frame3,
            textvariable=self.temp_var,
            font=fontStyleLarge,
            bg=bg_color,
            fg=text_color,
        )
        current_temp_lbl.pack(anchor = E, pady=(pad30,0), padx = (0, pad30))

        self.feels_like_var = StringVar()
        feels_like_lbl = Label(
            frame3,
            textvariable=self.feels_like_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        feels_like_lbl.pack(anchor = E, padx = (0, pad30))

        self.temp_max_min_var = StringVar()
        daily_max_min_lbl = Label(
            frame3,
            textvariable=self.temp_max_min_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        daily_max_min_lbl.pack(anchor = E, padx = (0, pad30))

        self.weather_desc_var = StringVar()
        desc_lbl = Label(
            frame3,
            textvariable=self.weather_desc_var,
            font=fontStyleMedium,
            bg=bg_color,
            fg=text_color,
        )
        desc_lbl.pack(anchor = E, padx = (0, pad30), pady=(10, 0))

        self.humidity_var = StringVar()
        humidity_lbl = Label(
            frame3,
            textvariable=self.humidity_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        humidity_lbl.pack(anchor = E, padx = (0, pad30), pady = (0, 10))

        self.wind_speed_var = StringVar()
        wind_speed_lbl = Label(
            frame3,
            textvariable=self.wind_speed_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        wind_speed_lbl.pack(anchor = E, padx = (0, pad30))
        self.wind_gust_var = StringVar()
        wind_gust_lbl = Label(
            frame3,
            textvariable=self.wind_gust_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        wind_gust_lbl.pack(anchor = E, padx = (0, pad30))

        # ##TODO: (HIGH priority)need to implement a .remove method for the label so that each image doesn't get stacked on top
        self.img_path_var = StringVar()
        if self.img_path_var.get():
            self.weather_img = ImageTk.PhotoImage(
                Image.open(self.img_path_var.get()).resize((95, 95))
            )
            self.weather_img_lbl = Label(frame3, image=self.weather_img, borderwidth=0)
            self.weather_img_lbl.pack(anchor = E, padx = (0, pad30))

        self.update_thread = Thread(target=self.get_weather(cfd))
        self.update_thread.daemon = True
        self.update_thread.start()

        self.aqi_var = StringVar()
        aqi_lbl = Label(
            frame6,
            textvariable=self.aqi_var,
            font=fontStyleSmall,
            bg=bg_color,
            fg=text_color,
        )
        aqi_lbl.pack(side="left",  padx = pad30/3)

        self.aqi_color = StringVar()
        self.canvas = Canvas(frame6, background=bg_color, highlightthickness=0, height = 21, width = 21)
        self.circle = self.canvas.create_oval(0,0,21,21, outline = bg_color, width = 2)
        self.canvas.pack(side="left", anchor = E, padx = (0, pad30))

        self.update_thread = Thread(target=self.get_aqi(cfd))
        self.update_thread.daemon = True
        self.update_thread.start()

    def get_date_time(self):
        self.dow_var.set(datetime.today().strftime("%A"))
        self.date_var.set(datetime.today().strftime("%B %d, %Y"))
        self.time_var.set(datetime.now().strftime("%H:%M"))

        self.after(1000, self.get_date_time)

    def get_weather_icon_path(self, weather_desc):
        # maps open weather icons to weather conditions, see https://openweathermap.org/weather-conditions
        ##TODO: (low priority)implement logic for clear day/night and cloudly day/night (something having to do with sunrise or sunset)
        __icon_lookup = {
            "clear": "imgs/Sun.png",
            # "clear-sky": "imgs/Sun.png",  # clear sky day
            # "clear-night": "imgs/Moon.png",  # clear sky night
            "clouds": "imgs/Cloud.png",  # cloudy day
            # "partly-cloudy-day": "imgs/PartlySunny.png",  # partly cloudy day
            # "partly-cloudy-night": "imgs/PartlyMoon.png",  # scattered clouds night
            "thunderstorm": "imgs/Storm.png",  # thunderstorm
            "drizzle": "imgs/Rain.png",  # rain day
            "rain": "imgs/Rain.png",  # rain day
            "snow": "imgs/Snow.png",  # snow day
            "mist": "imgs/Haze.png",
            "smoke": "imgs/Haze.png",
            "haze": "imgs/Haze.png",
            "dust": "imgs/Haze.png",
            "fog": "imgs/Haze.png",  # fog day
            "sand": "imgs/Haze.png",
            "ash": "imgs/Haze.png",
            "squall": "imgs/Haze.png",
            "tornado": "imgs/Tornado.png",  # tornado
        }

        return __icon_lookup[weather_desc]

    def get_weather(self, config):
        ## Make GET request
        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={config._weather_zip_code}&appid={config._weather_api_key}&units=imperial"
        )

        try:
            r_weather = requests.get(weather_req_url)
            weather_obj = r_weather.json()

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

        self.humidity_var.set("Humidity: " + str(weather_obj["main"]["humidity"]) + "%")


        self.wind_speed_var.set(
            "Wind: " + str(weather_obj["wind"]["speed"]) + " mph")
        if "gust"  in weather_obj["wind"]:
            self.wind_gust_var.set(
                "Gusts: " + str((weather_obj["wind"]["gust"]) + " mph"))

        self.weather_desc_var.set(weather_obj["weather"][0]["main"])

        self.img_path_var.set(
            self.get_weather_icon_path(self.weather_desc_var.get().lower())
        )

        self.sun_rise_set_var.set(
            "Rise "
            + datetime.fromtimestamp(weather_obj["sys"]["sunrise"]).strftime("%H:%M")
            + " | "
            + "Set  "
            + datetime.fromtimestamp(weather_obj["sys"]["sunset"]).strftime("%H:%M")
        )

        self.after(900000, self.get_weather, cfd)  # 900000ms = 15 minutes

    def get_aqi(self, config):
        aqi_req_url = str(
            f"http://api.openweathermap.org/data/2.5/air_pollution?lat={config._weather_lat}&lon={config._weather_lon}&appid={config._weather_api_key}"
        )

        try:
            r_aqi = requests.get(aqi_req_url)
            aqi_obj = r_aqi.json()

        except requests.exceptions.RequestException as e:
            print("Raise error:", e)

        aqi_cat = aqi_obj['list'][0]['main']['aqi']
        aqi_value_mapping = {1: "Good", 2: "Moderate", 3: "Unhealthy for Sensitive Groups", 4: "Unhealthy", 5: "Very Unhealthy", 6: "Hazardous"}
        self.aqi_var.set("AQI: " + aqi_value_mapping.get(aqi_cat, "Unknown"))

        aqi_color_mapping = {1: "#00E400", 2: "#FFFF00", 3: "#FF7E00", 4: "#FF0000", 5: "#8F3F97", 6: "#7E0023"}
        new_color = aqi_color_mapping.get(aqi_cat, "#808080")
        self.canvas.itemconfig(self.circle, fill=new_color)

        self.after(900000, self.get_aqi, cfd)  # 900000ms = 15 minutes

if __name__ == "__main__":
    root = tk.Tk()
    root.title("")
    root.configure(background="black")
    # root.wm_attributes("-fullscreen", "True") ##av.note really difficult to close (have to go to task manager); probably will use this in final version of gui
    root.state("zoomed")  # start app with maximized display

    app = Display(master=root)

    root.mainloop()
