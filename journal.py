from time import gmtime, strftime
import datetime
import re
import os


#
# def journal():
#     content = ""
#     infile = open("account.txt", "w")
#     infile.write(str(strftime("%a, %d %b %Y %H:%M:%S +0000,\n", gmtime())))
#     print("Input text: ")
#     while 1:
#         content = input()
#         if content == "exit":
#             break
#         infile.write(content + '\n')
#     infile.close()
#
#
# def read():
#     infile = open("account.txt", "r")
#     word = infile.read()
#     split = re.split('\n|,', word)
#     # split = word.split(',')
#     print(split)
#
#
# read()


# Create folder to contain journal
def create_journal():
    """
    Ask the user to name the journal
    Find the current directory we’re in so that we can create our
    journal in the same one
    Create the journal
    """

    journal_name = input("Input the name of journal: ")
    cwd = os.getcwd()  # Return a string representing the current working directory.
    path_file = cwd + '/' + journal_name  # set path to variable path_file

    try:
        os.mkdir(path_file)
    except OSError:
        print("Creation of the directory %s failed" % path_file)
    else:
        print("Create successfully %s" % path_file)


def open_journal():
    os.chdir(os.getcwd())
    journal_list = os.listdir()
    print("List of journal : {}".format(len(journal_list)))
    # Print all journal file
    for i in journal_list:
        print(i)
    journal_name = input("Please input the name of the journal: ")
    cwd = os.getcwd()
    path = cwd + "/" + journal_name
    os.chdir(path)

    page_list = os.listdir()
    print("Current pages:".format(len(page_list)))
    for page in page_list:
        print(page)


def write_content():
    content = input("Body: ")
    return content


#
# def add_page():
#     title = input("Input the title of journal: ")
#     author = input("Input the author of journal: ")
#     filename = title.replace(" ", "") + ".txt"  # Remove spaces in name
#     content = write_content()
#     input_file = open(filename, "a")
#     input_file.write(title + "\n")
#     input_file.write(author + "\n")
#     input_file.write(str(strftime("%a, %d %b %Y %H:%M:%S +0000,\n", gmtime())))
#
#     count = 0
#     prev_index = 0
#     for i in range(0, len(content) - 1):
#         if content[i] == " ":
#             input_file.write(content[prev_index:i])
#             count += 1
#             prev_index = i
#         if count == 10:
#             count = 0
#             input_file.write("\n")
#
#     input_file.close()
#

def add_content():
    title = input("What's the title of your entry?  ")
    content = write_content()
    filename = title.replace(" ", "") + ".txt"
    entry = open(filename, "a")
    entry.write(author + "\n")
    entry.write(title + "\n")
    entry.write(str(datetime.datetime.now()) + "\n")

    count = 0
    prev_index = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[prev_index:i])
            count += 1
            prev_index = i
        if count == 10:
            count = 0
            entry.write("\n")

    entry.close()


def remove_page():
    title = input("What's the title of your entry?  ")
    filename = title.replace(" ", "") + ".txt"
    os.remove(filename)


def menu():
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Create a page")
    print("4: Remove_page")
    option = input("Your choice:  ")
    print("-----\n-----")
    if option == "1" or option == 1:
        create_journal()
    elif option == "2" or option == 2:
        open_journal()
    elif option == "3" or option == 3:
        add_content()
    elif option == "4" or option == 4:
        remove_page()
    else:
        print("Please input 1-4 options")
        menu()
    choice = input("Do you need to select anything else? (Y/N)")
    if choice == "y" or choice == "yes" or choice == "Y":
        menu()
    else:
        print("Bye Bye <3")


author = input("What's your name?  ")
menu()
