class Student:
    def __init__(self):
        self.ID = 587022
        self.fname = 'Chai'
        self.lname = 'Dev'
        self.__score = 40
    
    def ShowData(self):
        print(self.ID, self.fname, self.lname, self.__score)
        
    def __updateData(self, degree):
        self.degree = degree
        print(self.ID, self.fname, self.lname, self.__score, self.degree)
        
std = Student()
std.ShowData()
std.__score = 50
std._Student__updateData('Master')
std._Student__score = 80
std._Student__updateData('Master')