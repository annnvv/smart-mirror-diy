from datetime import datetime
from tkinter import *


def get_clock_info(self):
    """Generate Day of Week, Date, and Time information"""

    self.dow = datetime.today().strftime("%A")
    self.date = datetime.today().strftime("%B %d, %Y")
    self.time = datetime.now().strftime("%H:%M:%S")

    self.after(200, self.get_clock_info)
