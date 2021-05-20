from journal import Journal

import datetime
import os


class Page(Journal):
    def __init__(self):
        super(Page, self).__init__()
        self.page_name = ""
        self.content = ""

    def set_page_name(self, page_name):
        self.page_name = page_name

    def open_page(self):
        self.set_page_name(input("Input the page name: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        entry = open(filename, "r")
        print(*entry)

    def write(self):
        self.content = input("Body: ")
        return self.content

    def add_content(self):
        self.set_page_name(input("Input the page name: "))
        self.set_title(input("Input the title: "))
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
            self.open_page()

        else:
            print("bye")

    def remove(self):
        self.set_page_name(input("Input the name of a page: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        os.remove(filename)
