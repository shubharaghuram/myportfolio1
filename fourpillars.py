class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Shape):
    def __init__(self,s1):
           self.s1 = s1
        
    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)
a_rectangle.what_am_i()
a_square.what_am_i()

"""class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("created!")

    def rot(self,days,temp):
        self.mold = days*temp
        

or1 = Orange(9, "green")
print(or1.mold)
or1.rot(10,98)
print(or1.mold)
"""

