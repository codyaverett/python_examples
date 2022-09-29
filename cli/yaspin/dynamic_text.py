import time
from datetime import datetime
from yaspin import yaspin


class TimedText:
    def __init__(self, text):
        self.text = text
        self._start = datetime.now()

    def __str__(self):
        now = datetime.now()
        delta = now - self._start
        return f"{self.text} ({round(delta.total_seconds(), 1)}s)"


with yaspin(text=TimedText("time passed:")):
    time.sleep(3)
