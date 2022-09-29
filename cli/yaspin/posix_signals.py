import time

from yaspin import kbi_safe_yaspin


with kbi_safe_yaspin(text="Press Control+C to send SIGINT (Keyboard Interrupt) signal"):
    time.sleep(5)  # time consuming code
