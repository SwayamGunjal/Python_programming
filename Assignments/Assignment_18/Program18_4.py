#########################################################################################################
#   Function name   :   FreqElement
#   Description     :   Returns the frequency of the given element in the list. 
#   Input           :   List, Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def FreqElement(Data, Val):
    Count = 0
    
    for i in Data:
        if i == Val:
            Count += 1

    return Count
    

def main(): 
    
    Val1 = 0
    Size = 0
    Value = list()

    print("Enter the size of list : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter element for frequency count : ", end = "")
    Val1 = int(input())


    Ret = FreqElement(Data,Val1)
    
    print("Frequency of the given element is :",Ret)

#   Starter Condition
if __name__ == "__main__":
    main()