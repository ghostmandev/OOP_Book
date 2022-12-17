class Book:
    wide = 25
    high = 30
    page = 250
    
    def showBook(self, name, isbn):
        self.isbn = isbn
        self.name = name
        return self.name, Book.wide, Book.high, Book.page, self.isbn
    
b_it = Book()
b_web = Book()

print(format(b_it.showBook('Python Programmming', '123-456')))
print(format(b_web.showBook('Web Programmming', '999-888')))