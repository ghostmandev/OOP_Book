class Book:
    def __init__(self, name, size, page, price):
        self.name = name
        self.size = size
        self.page = page
        self.price = price
    
    def showBook(self):
        return self.name, self.size, self.page, self.price
    
class Book_IT(Book):
    pass

book = Book('Python Programming', '25x30', 280, 300)

b_it = Book_IT('Information Science', '25x32', 390, 250)

print(book.showBook())
print(b_it.showBook())
