from morse_codes import *
import tkinter as tk
from tkinter import messagebox

def conversion():
    text_to_convert = convert_entry.get().upper()
    converted_text = []
    for let in text_to_convert:
        if let == ' ':
            converted_text.append('/')
        elif let in MORSE_CODE_DICT:
            converted_text.append(MORSE_CODE_DICT[let])
        else:
            messagebox.showwarning('Error', f'{let} not in Morse Code')
    word_created = ' '.join(converted_text)
    converted_output.config(state='normal')
    converted_output.delete(0, tk.END)
    converted_output.insert(0, word_created)
    converted_output.config(state='readonly')

def reversion():
    code_to_revert = revert_entry.get()
    per_code = []
    temp = ''
    for char in code_to_revert:
        if char == '/':
            per_code.append(char)
        elif char != ' ':
            temp += char
        else:
            if temp:
                per_code.append(temp)
                temp = ''

    if temp:
        per_code.append(temp)

    message = []
    for code in per_code:
        code = code.strip()
        if code == '/':
            message.append(code)
        elif code in REVERSE_MORSE_CODE_DICT:
            message.append(REVERSE_MORSE_CODE_DICT[code])
        else:
            messagebox.showwarning('Error', f'{code} not in Morse Code')

    decoded_text = ''
    for code in message:
        if code == '/':
            decoded_text += ' '
        else:
            decoded_text += code
    reverted_output.config(state='normal')
    reverted_output.delete(0, tk.END)
    reverted_output.insert(0, decoded_text)
    reverted_output.config(state='readonly')

root = tk.Tk()
root.title("Morse Code Converter")

label = tk.Label(root, text="Morse Code Converter")
label.grid(column=0, row=0)

convert_button = tk.Button(text='Convert', command=conversion)
convert_button.grid(column=0, row=1)
convert_entry = tk.Entry(root, width=30, justify='left')
convert_entry.grid(column=1, row=1)
convert_label = tk.Label(root, text="Converted Text: ")
convert_label.grid(column=0, row=2)
converted_output = tk.Entry(root, width=30, state='readonly')
converted_output.grid(column=1, row=2)

revert_button = tk.Button(text='Revert', command=reversion)
revert_button.grid(column=0, row=3)
revert_entry = tk.Entry(root, width=30, justify='left')
revert_entry.grid(column=1, row=3)
revert_label = tk.Label(root, text="Reverted Text: ")
revert_label.grid(column=0, row=4)
reverted_output = tk.Entry(root, width=30, state='readonly')
reverted_output.grid(column=1, row=4)

root.mainloop()