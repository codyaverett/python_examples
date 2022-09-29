import time
from yaspin import yaspin, Spinner

# Compose new spinners with custom frame sequence and interval value
sp = Spinner(["😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀"], 200)

with yaspin(sp, text="Cat!"):
    time.sleep(3)  # cat consuming code :)
