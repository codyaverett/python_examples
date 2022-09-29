"""
  This program is designed to create
  and animate a simple loading animation.
"""

from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread

done = False

def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        terminal.write('\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\rDone!    ')
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(5)
done = True