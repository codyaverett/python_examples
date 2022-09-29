import time
from yaspin import yaspin

spinner = yaspin()
spinner.start()

time.sleep(3)  # time consuming tasks

spinner.stop()
