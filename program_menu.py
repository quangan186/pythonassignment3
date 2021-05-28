from journal import Journal
from page import Page
import os


def journal_menu(input_journal, input_page):
    """
    This function represent the menu of the journal
    :param input_journal: input the name of the journal
    :param input_page: input which page users want to go to
    :return: none
    """
    while True:
        print("What would you like to do?: ")
        print("1: Create a journal")
        print("2: Open a journal")
        print("3: Remove journal")
        print("EXIT to close the program")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            input_journal.create()
        elif option == "2":
            input_journal.open()
            page_menu(input_page)
        elif option == "3":
            input_journal.remove()
        elif option.lower() == "exit":
            return False
        else:
            print("Please input 1-3 options: ")


def page_menu(input_page):
    """
    This function represent the menu of the pages
    :param input_page: input the name of the page which users want to go to
    :return: none
    """
    while True:
        print("""
            1.Create page
            2.Display page
            3.Delete page
            4.Return to main menu
        """)
        option = input("Enter your option: ")
        if option == "1":
            input_page.add_content()
        elif option == "2":
            input_page.display()
        elif option == "3":
            input_page.remove()
        elif option == "4":
            os.chdir(origin)
            print("Back to main menu")
            return False
        else:
            print("Please input from 1->4")


# Menu
def spaceship_menu():
    """
    This function is used as a main menu to call other functions
    :return: none
    """
    while True:

        print("Menu")
        print("1. Check overall spaceship ")
        print("2. Exit")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == '1':
            from basic_info import distance_and_time_cal
            print(distance_and_time_cal(225000000))
        elif option == "2":
            print('Stop the process')
        else:
            print("Please input 1-2 options: ")

def main_menu(input_journal, input_page):
    """
    This function represent the menu of the journal
    :param input_journal: input the name of the journal
    :param input_page: input which page users want to go to
    :return: none
    """

    while True:

        print("What would you like to do?: ")
        print("1: Open Spaceship Dashboard")
        print("2: Open Journal Dashboard")
        print("3: Open Binary Clock")
        print("EXIT to close the program")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            spaceship_menu()
        elif option == "2":
            journal_menu(input_journal, input_page)
        elif option == "3":
            from binary import binary_clock
            binary_clock()
        elif option.lower() == "exit":
            return False
        else:
            print("Please input 1-3 options: ")


# The condition when users type '__main__' instead of a page name or a journal name
if __name__ == '__main__':
    journal = Journal()
    page = Page()
    author = input("Input your name: ")
    origin = os.getcwd()
    journal.set_author(author)
    page.set_author(author)
    print(""""
    ----------Welcome {} to HD spaceship------------
    Made by: 
    Nguyen Tuan Anh    (s3864077)
    Bui Quang An       (s3877482)
    Nguyen Ha Dieu Anh (s3879053)
    """.format(author))
    main_menu(journal, page)
