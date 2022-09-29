import time
from yaspin import yaspin
from yaspin.spinners import Spinners

text = "Bold blink magenta spinner on cyan color"
with yaspin().bold.blink.magenta.bouncingBall.on_cyan as sp:
    sp.text = text
    time.sleep(3)

# The same result can be achieved by passing arguments directly
with yaspin(
    Spinners.bouncingBall,
    color="magenta",
    on_color="on_cyan",
    attrs=["bold", "blink"],
) as sp:
    sp.text = text
    time.sleep(3)
