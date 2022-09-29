from prompt_toolkit import print_formatted_text, ANSI


# Some people like to use the VT100 ANSI escape sequences to generate output.
# Natively, this is however only supported on VT100 terminals, but prompt_toolkit
# can parse these, and map them to formatted text instances.
# This means that they will work on Windows as well.
# The ANSI class takes care of that.

# Keep in mind that even on a Linux VT100 terminal, the final output produced by
# prompt_toolkit, is not necessarily exactly the same. Depending on the color depth,
# it is possible that colors are mapped to different colors, and unknown tags
# will be removed.

print_formatted_text(ANSI('\x1b[31mhello \x1b[32mworld'))
