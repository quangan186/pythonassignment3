from time import gmtime, strftime
import re


def journal():
    content = ""
    infile = open("account.txt", "w")
    infile.write(str(strftime("%a, %d %b %Y %H:%M:%S +0000,\n", gmtime())))
    print("Input text: ")
    while 1:
        content = input()
        if content == "exit":
            break
        infile.write(content + '\n')
    infile.close()


def read():
    infile = open("account.txt", "r")
    word = infile.read()
    split = re.split('\n|,', word)
    # split = word.split(',')
    print(split)


read()
