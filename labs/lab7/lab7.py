"""
Name: Thomas Scola
I certify this is my work and my work only
lab7.py
"""
import math
def cash_conversion():
    cash = eval(input("Input cash amount"))
    cash_float = "{:.2f}".format(cash)
    print("$" +cash_float)

def encode():
    inputSentence = str(input("Please enter a string of plaintext:"))
    key_value = int(input("Please enter the value of the key:"))
    codedMessage = ""

    for ch in inputSentence:
        codedMessage += chr((ord(ch) - 97 + key_value) % 26 + 97)

    print("The text inputed", codedMessage)

def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return(volume)

def sum_n(n):
    accum = 0
    for num in range(n):
        accum += 1 ** 3
    return accum

def sum_n_cube(n):
    accum = 0
    for num in range(n):
        accum += num ** 3
    return accum

def encode_better():
    input_sentence = input("Please enter a string of plaintext:")
    key_value = input("Please enter the key:")
    codedMessage = ""

    for ch in range(len(input_sentence)):
        s = ord(input_sentence[ch])
        k = ord(key_value[ch % len(key_value)])
        k = k -97
        s = s + k
        new_sentence = chr(s)
        codedMessage += new_sentence

    print(codedMessage)


def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(3))
    print(sum_n_cube(3))
    encode_better()


main()
