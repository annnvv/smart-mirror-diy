# smartmirror.py

# from tkinter import *
from utils.display import displayWindow
from utils import text, read_yaml
from utils.weather import Weather

# from utils.train import Wmata
# from utils.clock import Clock

config = read_yaml()

weather = Weather()
# train = Wmata()

w = displayWindow()
w.root.mainloop()
