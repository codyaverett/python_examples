import time
from yaspin import yaspin

with yaspin(text="elapsed time", timer=True) as sp:
    time.sleep(3.1415)
    sp.ok()
