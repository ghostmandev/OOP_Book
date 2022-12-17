class Book:
    def __init__(self):
        self.name = ''
        self.wide = ''
        self.high = ''
        self.page = ''
        self.isbn = ''
        self.price = ''
        
    def showBook(self):
        return self.name, self.wide, self.high, self.page, self.isbn, self.price
    
b_linux = Book()
b_linux.name = 'Linux Programming'
b_linux.wide = 25
b_linux.high = 30
b_linux.page = 350
b_linux.isbn = '111-222'
b_linux.price = 300

b_DB = Book()
b_DB.name = 'Database Programming'
b_DB.wide = 30
b_DB.high = 35
b_DB.page = 377
b_DB.isbn = '999-888'
b_DB.price = 350

print(b_linux.showBook())
print(b_DB.showBook())

print(b_linux.page)