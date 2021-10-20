"""
Name:Thomas Scola
vigenere.py
Problem: to make a vigenere cipher
Certification of Authenticity: I certify that this is entirely my own work.

"""
from graphics import *

def draw_button(point_1, point_2, button_text, win):
    outline = Rectangle(point_1, point_2)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)

def input(message):
    message = message.upper()
    message = message.replace(" ", "")
    return message

def code(message, keyword):
    sentence = input(message)
    ky_wrd = input(keyword)
    key_list = []
    for i in range(len(sentence)):
        sen = sentence[i]
        key = i % len(ky_wrd)
        converter = ord(sen) - 65
        encryption = ord(ky_wrd[key]) - 65
        encoder = chr(((converter + encryption) % 26) +65)
        key_list.append(encoder)
    text = "".join(key_list)
    return text

def main():
    win = GraphWin("Vigenere Encryption", 600, 600)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(1, 3), " Message to code: ").draw(win)
    Text(Point(1, 2.5), "Enter the Keyword: ").draw(win)

    message = Entry(Point(2.25, 3), 5)
    message.setText(" ")
    message.draw(win)
    msg = str(message)

    keyword = Entry(Point(2.25, 2.5), 5)
    keyword.setText(" ")
    keyword.draw(win)
    key = str(keyword)

    button = Text(Point(1.5, 1), "Encode")
    button.draw(win)
    Rectangle(Point(1, 0.5), Point(2, 1.5)).draw(win)

    win.getMouse()
    encoded_text = Text(Point(1, 2), code(msg, key))
    encoded_text.draw(win)


if __name__ =='__main__':
    main()
