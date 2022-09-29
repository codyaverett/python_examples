import os
import time
from signal import SIGTERM, SIGUSR1

from yaspin import yaspin
from yaspin.signal_handlers import default_handler, fancy_handler


sigmap = {SIGUSR1: default_handler, SIGTERM: fancy_handler}
with yaspin(sigmap=sigmap, text="Handling SIGUSR1 and SIGTERM signals") as sp:
    sp.write("Send signals using `kill` command")
    sp.write("E.g. $ kill -USR1 {0}".format(os.getpid()))
    time.sleep(20)  # time consuming code
