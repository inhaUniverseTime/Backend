class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def print(self):
        print("Rectangle 생성")
        print('Length = ', self.length,',Width = ', self.width, ',Area = ', self.length*self.width, ',parameter = ',2*(self.length + self.width))
class Box(Rectangle):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def print(self):
        print("Box 생성")
        print('Length = ', self.length,',Width = ', self.width, 'Height = ', self.height, ',Area = ', 2 * (self.length*self.width) + 2 * (self.height*self.width) + 2 * (self.length*self.height), ',Volume = ',self.height * self.length * self.width)


if __name__ =="__main__":
    r = Rectangle(10,20)
    r.print()

    b = Box(10,20,30)
    b.print()