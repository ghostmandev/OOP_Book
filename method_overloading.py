class Mobile:
    def __init__(self):
        self.brand = 'Samsung'
    
    def openMobile(self):
        return 'Open mobile with Slide'
    
    def __str__(self):
        return '{}, {}'.format(self.brand, self.openMobile())
    
class MobileOne(Mobile):
    def __init__(self):
        super().__init__()
    
    def openMobile(self):
        return 'Open mobile with Slide or Finger scan'

class MobileTwo(MobileOne):
    def __init__(self):
        super().__init__()
        
    def openMobile(self):
        return 'Open mobile with Slide, Finger scan or Face scan'

mobile = Mobile()
mobileOne = MobileOne()
mobileTwo = MobileTwo()

mobileOne.brand = 'Samsung A8'
mobileTwo.brand = 'Samsung A10'

print(mobile)
print(mobileOne)
print(mobileTwo)