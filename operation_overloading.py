class StudentTest:
    def __init__(self, score):
        self.score = score
    
    def __add__(self, other):
        result = self.score + other.score
        return StudentTest(result)
    
    def __str__(self):
        return "Total of score = {}".format(self.score)
    
score1 = StudentTest(20) # instance 
score2 = StudentTest(30) # instance 
score3 = StudentTest(25) # instance 
sumScore = score1 + score2 + score3
print(sumScore)