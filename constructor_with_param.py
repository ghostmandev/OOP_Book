class Book:
    def __init__(self, name, wide, high, page, isbn, price):
        self.name = name
        self.wide = wide
        self.high = high
        self.page = page
        self.isbn = isbn
        self.price = price
        
    def showBook(self):
        return self.name, self.wide, self.high, self.page, self.isbn, self.price
    
b_it = Book('Python Programming', 25, 30, 350, '123-456', 300)
print(b_it.showBook())

b_it.price = 350
print(b_it.showBook())

b_web = Book('Web Programming', 20, 25, 300, '999-888', 375)
print(b_web.showBook())