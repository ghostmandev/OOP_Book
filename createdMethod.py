class Calculate_area:
    def cal_rectangular(self, w, h):
        return w * h
    
    @classmethod
    def cal_triangle(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def cal_circle(r):
        import math
        return math.pi * r

cal = Calculate_area()
cal_rec = cal.cal_rectangular(3, 5)

cal_tri = Calculate_area.cal_triangle(6, 7)

cal_cir = Calculate_area.cal_circle(5)

print(f'Rectangular Area = {cal_rec}')
print(f'Triangle Area = {cal_tri}')
print(f'Circle Area = {cal_cir}')