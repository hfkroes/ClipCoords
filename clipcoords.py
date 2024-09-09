from pynput.keyboard import Key, Controller
import pyperclip
import time
import re

# Function to convert period to comma and prepare the output
def process_clipboard():
    clipboard_content = pyperclip.paste()
    if re.match(r'^-?\d+\.\d+,\s*-?\d+\.\d+$', clipboard_content):
        print("Pattern match!")
        # Convert periods to commas in numbers
        converted = clipboard_content.replace('.', ',')
        
        # Split into two numbers based on the comma
        split_values = converted.split(', ')
        
        # Format to tab-separated, so it will paste into two Excel cells
        formatted_output = f"{split_values[0]}\t{split_values[1]}"
        
        # Copy the formatted output back to clipboard
        pyperclip.copy(formatted_output)
        print(f"Processed and copied to clipboard:\n{split_values[0]}\n{split_values[1]}")

# Monitoring clipboard changes
def monitor_clipboard():
    recent_value = pyperclip.paste()
    print(f"Current clipboard: {recent_value}")
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            print("Clipboard checked: value changed!")
            print(f"Current clipboard: {tmp_value}")
            recent_value = tmp_value
            process_clipboard()
        time.sleep(1)
        print("Clipboard checked: no changes...")

if __name__ == "__main__":
    print("Script working: scanning clipboard!")
    monitor_clipboard()