#########################################################################################################
#   Function name   :   ElementSum
#   Description     :   Calculates and prints the sum of digits of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

def ElementSum(Data):
    Sum = 0
    
    for i in Data:
        Sum = Sum + Data
    print(Sum)


def main(): 
    
    Size = 0
    Value = list()

    print("Enter the size of list : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Entered list : ",Data)

    ElementSum(Data)
  
    
#   Starter Condition
if __name__ == "__main__":
    main()