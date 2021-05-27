from journal import Journal

import datetime
import os


class Page(Journal):
    def __init__(self):
        """
        constructor of the task
        """
        super(Page, self).__init__()
        self.page_name = ""
        self.content = ""

    def set_page_name(self, page_name):
        """
        getter of the task
        :param page_name: set a name for a page
        :return: none
        """
        self.page_name = page_name

    def open_page(self):
        """
        open a page
        :return: none
        """
        self.set_page_name(input("Input the page name: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        entry = open(filename, "r")
        print(*entry)

    def write(self):
        """
        write a body of a note/paragraph or any kind of text in a page
        :return: self.content
        """
        self.content = input("Body: ")
        return self.content

    def add_content(self):
        """
        this function is used to add content on a page
        :return: none
        """
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
        """
        display a page on the list
        :return: none
        """
        page_list = os.listdir()
        print("Current pages:".format(len(page_list)))
        print(*page_list)
        option = input("Do you wanna open da file (Y/N): ")
        if option == "Y":
            self.open_page()

        else:
            print("bye")

    def remove(self):
        """
        Remove a page from the list
        :return: none
        """
        self.set_page_name(input("Input the name of a page: "))
        filename = self.page_name.replace(" ", "") + ".txt"
        os.remove(filename)
