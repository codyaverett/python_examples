import sys
import time

from yaspin import yaspin
from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style

# override print with feature-rich ``print_formatted_text`` from prompt_toolkit
print = print_formatted_text

# build a basic prompt_toolkit style for styling the HTML wrapped text
style = Style.from_dict({
    'msg': '#4caf50 bold',
    'sub-msg': '#616161 italic'
})


with yaspin(text='Downloading images') as sp:
    # task 1
    time.sleep(1)
    with sp.hidden():
        print(HTML(
            u'<b>></b> <msg>image 1</msg> <sub-msg>download complete</sub-msg>'
        ), style=style)

    # task 2
    time.sleep(2)
    with sp.hidden():
        print(HTML(
            u'<b>></b> <msg>image 2</msg> <sub-msg>download complete</sub-msg>'
        ), style=style)

    # finalize
    sp.ok()
