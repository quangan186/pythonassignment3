import datetime
import os


class Journal:
    def __init__(self):
        self.title = ""
        self.author = ""

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def create(self):
        self.set_title(input("Input the journal name: "))
        cwd = os.getcwd()  # Return a string representing the current working directory.
        path_file = cwd + '/' + self.title  # set path to variable path_file
        try:
            os.mkdir(path_file)
        except OSError:
            print("Creation of the directory %s failed" % path_file)
        else:
            print("Create successfully %s" % path_file)

    def open(self):

        os.chdir(os.getcwd())

        print("List of journal : {}".format(len(os.listdir())))
        print(*os.listdir())
        self.set_title(input("Input the journal name: "))
        os.chdir(os.getcwd() + "/" + self.title)

        page_list = os.listdir()
        print("Current pages:".format(len(page_list)))
        for page in page_list:
            print(page)

    def remove(self):
        self.set_title(input("Input the name of journal: "))
        os.remove(self.title)


class Page(Journal):
    def __init__(self):
        super(Page, self).__init__()
        self.page_name = ""
        self.content = ""

    def set_page_name(self, page_name):
        self.page_name = page_name

    def open(self):
        self.set_page_name(input("Input the page name: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        entry = open(filename, "r")
        for i in entry:
            print(i)

    def write(self):
        self.content = input("Body: ")
        return self.content

    def add_content(self):
        self.set_page_name(input("Input the page name: "))
        self.content = self.write()
        filename = self.page_name.replace(" ", "") + ".txt"
        entry = open(filename, "a")
        entry.write(self.author + "\n")
        entry.write(self.title + "\n")
        entry.write(str(datetime.datetime.now()) + "\n")
        entry.write(self.content)
        entry.close()

    def display(self):
        page_list = os.listdir()
        print("Current pages:".format(len(page_list)))
        print(*page_list)
        option = input("Do you wanna open da file (Y/N): ")
        if option == "Y":
            self.open()
        else:
            print("Back to menu.")

    def remove(self):
        self.set_page_name(input("Input the name of a page: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        os.remove(filename)


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
