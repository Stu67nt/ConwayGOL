from colorama import just_fix_windows_console  # Fixes Issue with ANSII codes not working

def main():
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    # ANSII escape character. Moves cursor to the top of the terminal and clears everything below cursor
    print("\033[H\033[3J", end="")
    print(frame, flush=True)