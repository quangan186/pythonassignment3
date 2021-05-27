from journal import Journal
from page import Page
import os


def menu(input_journal, input_page):
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


# The condition when users type '__main__' instead of a page name or a journal name
if __name__ == '__main__':
    journal = Journal()
    page = Page()
    author = input("Input your name: ")
    origin = os.getcwd()
    journal.set_author(author)
    page.set_author(author)

    menu(journal, page)
