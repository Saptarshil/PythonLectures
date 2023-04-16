class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  #when the book oject is printed, the information is displayed. str basically converts the anything to string and returns it.
        return "Author:{},Title:{},Pages:{}".format(self.author, self.title, self.pages)

    def __len__(self):  #to figure out the lenght of the book object, the no of pages is returned. if this method is not overriden but is called, an error message will pop up.
        return self.pages

    def __del__(self):  #At the time the book object is deleted, this message is printed
        print("Book Object is deleted")


new_book = Book("Mashe", "Isaki Makumoto", 273)  #new object is created
print(str(new_book))  #these dunder methods have been overridden here. Comment out the overriden methods to see the actual result.
print((len(new_book)))
print(new_book)  #print converts its value to string and return it to the console. the str method is overriden and hence this output is shown.
del new_book  #generally taken care by the garbage collector.
