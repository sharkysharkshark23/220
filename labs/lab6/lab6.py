"""
Name: Thomas Scola
lab6.py
This program is designed to work with string manipulation
I certify this is my work and my work only
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    wholename = input("Please enter your name lastname, firstname: ")
    answer = wholename.split()
    print("Your name is ", answer)



def company_name():
    website = input("Enter a website: ")
    website = website.split(".")
    print(website[1])

def initials():
    numbernames = eval(input("Enter the number of names there are: "))
    for num in range(numbernames):
        firstname = input("Enter the initial of the first name " +str(num + 1))
        lastname = input("Enter the initial of the last name " +str(num + 1))
        initials = firstname[0] + lastname[0]
        print(firstname+ "initials are ", initials)

def names():
    names = input("Enter names")
    names = names.split(",")
    for name in names:
        name = name.split()
        first = name[0]
        last = name[1]
        print(first[0] + last[0])

def thirds():
    sentence = input("Enter your sentence")
    print(sentence[2::3])

def word_average():
    acc = 0
    sentence = input("input the sentence: ")
    sentence = sentence.split("list of words")
    for word in sentence:
        acc += len(word)
    print(acc / len(sentence))

def pig_latin():
    sentence = input("Input your sentence: ")
    sentence = sentence.lower()
    sentence = sentence.split(" ")
    for word in sentence:
        encoder = word[1:] + word[0] + "ay"
        print(encoder, end=" ")

def main():
    name_reverse()
#   # add other fucntion calls here
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

main()




