from journal import Journal
from page import Page


def menu(input_journal, input_page):
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Remove journal")
    print("EXIT to close the program")
    option = input("Your choice:  ")
    print("-----\n-----")
    if option == "1":
        input_journal.create()
    elif option == "2":
        input_journal.open()
        page_menu(input_page)
    elif option == "3":
        input_journal.remove()
    elif option.lower() == "exit":
        print("Bye Bye <3")
    else:
        print("Please input 1-3 options")
        menu(input_journal)
    choice = input("Do you need to select anything else? (Y/N) ")
    if choice == "y" or choice == "yes" or choice == "Y":
        menu(input_journal, input_page)
    else:
        print("Bye Bye <3")


def page_menu(input_page):
    print("""
        1.Create page
        2.Display page
        3.Delete page
        4.Return to main menu
    """)
    option = int(input("Enter your option: "))
    if option == 1:
        input_page.add_content()
    elif option == 2:
        input_page.display()
    elif option == 3:
        input_page.remove()
    elif option == 4:
        print("Bye")
    else:
        choice = input("Do you need to select anything else? (Y/N) ")
        if choice == "y" or choice == "yes" or choice == "Y":
            input_page.page_menu()
        else:
            print("Bye")


if __name__ == '__main__':
    journal = Journal()
    page = Page()
    author = input("Input your name: ")
    journal.set_author(author)
    page.set_author(author)

    menu(journal, page)
