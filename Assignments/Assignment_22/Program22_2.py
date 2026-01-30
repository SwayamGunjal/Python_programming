########################################################################################################################
#
#   Class name      :   Circle
#   Description     :   Implement a class to calculate and display area and
#                       circumference of a circle using class variable PI.
#   Input           :   Float
#   Output          :   Void
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter Radius :")
        self.Radius = int(input())

    def CalculateArea(self):
        self.Area = 0

        self.Area = Circle.PI * (self.Radius**2)
    
    def Display(self):
        print("Radius of Circle : ",self.Radius)
        print("Area of Circle : ",self.Area)
        print("Circumference of Circle : ",self.Circumference)

def main():

    Obj1 = Circle()

    Obj1.Accept()

    Obj1.CalculateArea()

    Obj1.CalculateCircumference()

    Obj1.Display()

if __name__ == "__main__":
    main() 