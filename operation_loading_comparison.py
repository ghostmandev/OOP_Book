class Compare:
    def __init__(self, x):
        self.x = x
    
    def __ge__(self, other):
        if (self.x >= other.x):
            return 'num1 is greater than or equal num2'
        else:
            return 'num1 is less than num2'
        
    def __ne__(self, other):
        if (self.x != other.x):
            return 'Both are not equal'
        else:
            return 'Both are equal'

num1 = Compare(200)
num2 = Compare(450)
result_n = num1 >= num2
print('The result of comparison is = ',result_n)

str1 = Compare('Python')
str2 = Compare('Java')
result_s = str1 == str2
print('The result of comparision is ',result_s)