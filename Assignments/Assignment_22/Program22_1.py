########################################################################################################################
#
#   Class name      :   Demo
#   Description     :   Implement a class with two instance variables, one class variable,
#                       constructor, and two instance methods to display instance data.
#   Input           :   Integer, Integer
#   Output          :   Void
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class Demo:
    Value = 10

    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("Inside Fun")
        print("Instance Variable no1 :", self.no1)
        print("Instance Variable no2 :", self.no2)

    def Gun(self):
        print("Inside Gun")
        print("Instance Variable no1 :", self.no1)
        print("Instance Variable no2 :", self.no2)

def main():
    Val1 = 0
    Val2 = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())
    
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()