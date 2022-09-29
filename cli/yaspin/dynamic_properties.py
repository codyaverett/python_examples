import time
from yaspin import yaspin
from yaspin.spinners import Spinners

with yaspin(Spinners.noise, text="Noise spinner") as sp:
    time.sleep(2)

    sp.spinner = Spinners.arc  # spinner type
    sp.text = "Arc spinner"    # text along with spinner
    sp.color = "green"         # spinner color
    sp.side = "right"          # put spinner to the right
    sp.reversal = True         # reverse spin direction

    time.sleep(2)
