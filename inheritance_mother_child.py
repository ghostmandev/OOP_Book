class Book:
    def __init__(self, name, size, page, price):
        self.name = name
        self.size = size
        self.page = page
        self.price = price
        
    def showBook(self):
        return self.name, self.size, self.page, self.price
    
class Book_IT(Book):
    def __init__(self, name, size, page, price, isbn, publisher):
        super().__init__(name, size, page, price)
        self.isbn = isbn
        self.publisher = publisher
        
    def showBook_IT(self):
        return super().showBook(), self.isbn, self.publisher
    
book = Book('Python Programing', '25x30', 275, 300)
b_IT = Book_IT('Information Technology', '25x32', 390, 250, '123-456', 'ABC')

print(book.showBook())
print(b_IT.showBook())