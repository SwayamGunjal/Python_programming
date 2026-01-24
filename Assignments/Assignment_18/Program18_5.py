#########################################################################################################
#   Function name   :   ListPrime
#   Description     :   Returns the addition of all prime numbers from the given list.
#   Input           :   List
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

import MarvellousNum   

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if MarvellousNum.ChkPrime(i) == True:
            Sum = Sum + i
    
    return Sum

def main(): 
    
    Val1 = 0
    Size = 0
    Value = list()

    print("Number of elements : ")
    Size = int(input())

    Data = list()

    print("Elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret1 = ListPrime(Data)

    print("Addition of Prime numbers : ",Ret1)

    
    


#   Starter Condition
if __name__ == "__main__":
    main()