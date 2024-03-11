#!/usr/bin/env python3




class Book:
    def __init__(self, title, page_count):
        self.title = title
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count_value):
        if type(page_count_value) == int:
            self.page_count = page_count_value
        else:
            print("page_count must be an integer")


book = Book("And Then There Were None", 272)
book.page_count = "rr"
    
        
    
        