# 🔠 Morse Code Converter (Tkinter GUI)
A simple graphical user interface (GUI) application built with Python and Tkinter that allows users to convert English text to Morse code and revert Morse code back to English.

📌 Features
✅ Convert English text to Morse code

✅ Revert Morse code back to readable English text

✅ Basic error handling for invalid characters or unknown Morse codes

✅ Clean and intuitive GUI using Tkinter

```
+--------------------------+
| Morse Code Converter     |
| [Convert]  [Input Text]  |
| Converted Text: [Output] |
| [Revert]   [Morse Input] |
| Reverted Text: [Output]  |
+--------------------------+
```
📦 Requirements
Python 3.x

Tkinter (usually comes with Python)

A separate Python module morse_codes.py containing the dictionaries:

MORSE_CODE_DICT: for conversion from text to Morse code

REVERSE_MORSE_CODE_DICT: for conversion from Morse code to text

Example morse_codes.py:
```python
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
```
🚀 How to Run
Clone or download the repository.

Make sure morse_codes.py is in the same directory as your main script.

Run the program using Python:
```bash
python morse_converter_gui.py
```
📝 Notes
Use / to represent spaces between words in Morse code.

Only English alphabets and numbers are supported in this version.

