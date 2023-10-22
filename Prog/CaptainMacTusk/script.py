#!/usr/bin/env python3
# =================================================================================
# Name: mocr.py (Morse OCR)
# Version: v2 (alpha)
# Author: eauxfolles
# Date: 10.07.2020
# Description: Script to read morse code from file and translate into readable text
# Usage: "mocr.py <image>"
# Assumptions:  - Morse code expected to be reflected as "." and "-"
#               - "." expected to be 1 pixel, "-" expected to be 3 pixel long
#               - Image has consistent background color (as pixel at position 0,0)
#               - Background color is different than morse code
#               - Each line contains one word coded in morse
# =================================================================================

import hashlib
from PIL import Image
import requests
import base64

s = requests.session()
data = s.get("https://capitainmactusk.flag4all.sh/index.php")
img = data.content.split(b" ")[2]
with open("morse.png", 'wb') as f:
    f.write(base64.b64decode(img.decode()))

num = data.content.split(b" ")[0].split(b"<")[0].decode()

translate = {
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.-.-.-': '.',
    '--..--': ',',
    '---...': ':',
    '-.-.-.': ';',
    '..--..': '?',
    '-.-.--': '!',
    '-....-': '-',
    '..--.-': '_',
    '-.--.': '(',
    '-.--.-': ')',
    '.----.': '\'',
    '.-..-.': '\"',
    '-...-': '=',
    '.-.-.': '+',
    '-..-.': '/',
    '.--.-.': '@'
}

image_file = "morse.png"
# use module "PIL" (Python Image Library) to open image-file and load image-data (size and background color) 
try:
    morse_image = Image.open(image_file)
except:
    print("error: could not open file")
    exit()
width, height = morse_image.size
pixel_data = morse_image.load()
background_color = pixel_data[0,0]

# define function to translate morse character into letter
def morse_translate(morse_input):
    try:
        return translate[morse_input]
    except:
        return "µ"
        # print("\nerror: unable to translate morse code")
        # exit()

# loop through each pixel, line after line
lines = []
for line in range(0, height):
    morse_char = ""
    pixel_count = 0
    morse_inline = 0
    background = 0
    new_line = []
    mot = ""
    for pixel in range(0, width):
        if pixel_data[pixel, line] != background_color:
            pixel_count += 1
            morse_inline = 1
            if background > 4:
                # print(background, morse_char)
                new_line.append(mot)
                mot = ""
            background = 0
        else:
            if pixel_count == 1:
                morse_char += "."
                if pixel_data[pixel+1, line] == background_color: 
                    mot += morse_translate(morse_char)
                    morse_char = ""
            elif pixel_count == 3:
                morse_char += "-"
                if pixel_data[pixel+1, line] == background_color: 
                    mot += morse_translate(morse_char)
                    morse_char = ""
            elif pixel_count == 0:
                pass
            else:
                print("error: cannot read morse code")
            pixel_count = 0
            background += 1
    if morse_inline != 0:
        new_line.append(mot)
        new_line = new_line[1:]
        lines.append(new_line)


m = ""

for i in range(len(num)):
    m += lines[i][int(num[i])]
md = hashlib.md5(m.encode()).hexdigest()

d = s.get("https://capitainmactusk.flag4all.sh/index.php/index.php?rep=" + md)
print(d.content.decode())


# close image-file
morse_image.close()