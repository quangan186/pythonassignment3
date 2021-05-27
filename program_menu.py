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
    print("Menu")
    print("1. Check overall spaceship ")
    print("2. Check health of spaceship")
    print("3. Check health of crew members")
    print("4. Exit")

    choose_button = input("Which one do you want to choose: ")
    if choose_button == '1':
        from basic_info import distance_and_time_cal
        print(distance_and_time_cal(230000000))
    elif choose_button == '2':
        from basic_info import spaceship_health
        print(spaceship_health(problems={"fan": 20, "heat": 30, "vision": 40, "radar": 40}))
    elif choose_button == '3':
        from basic_info import health_of_crew_members
        print(health_of_crew_members(10))

    else:
        print('Stop the process')


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
        print("3: Open Clock Dashboard")
        print("EXIT to close the program")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            spaceship_menu()
        elif option == "2":
            journal_menu(input_journal, input_page)
        elif option == "3":
            print("Maintain")
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
    main_menu(journal, page)
