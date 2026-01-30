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
        self.No1 = A
        self.No2 = B

    def fun(self):
        print("Inside fun")
        print("Instance Variable No1 :", self.No1)
        print("Instance Variable No2 :", self.No2)

    def gun(self):
        print("Inside gun")
        print("Instance Variable No1 :", self.No1)
        print("Instance Variable No2 :", self.No2)

def main():
    Val1 = 0
    Val2 = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())
    
    Obj1 = Demo(Val1, Val2)
    Obj2 = Demo(10, 50)

    Obj1.fun()

    Obj2.fun()

    Obj1.gun()

    Obj2.gun()

if __name__ == "__main__":
    main()