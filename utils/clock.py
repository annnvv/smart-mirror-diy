from datetime import datetime


class Clock:
    def get_clock_info(self) -> None:
        """Generate Day of Week, Date, and Time information"""

        self.dow = datetime.today().strftime("%A")
        self.date = datetime.today().strftime("%B %d, %Y")
        self.time = datetime.now().strftime("%H:%M")

        return None
