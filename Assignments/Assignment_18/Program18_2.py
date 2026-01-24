#########################################################################################################
#   Function name   :   MaxElement
#   Description     :   Returns the largest element in the list. 
#   Input           :   List
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def MaxElement(Data):
    Max = Data[0]
    
    for i in Data:
        if i > Max:
            Max = i

    return Max
    

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


    Ret = MaxElement(Data)
    
    print("Max : ",Ret)

#   Starter Condition
if __name__ == "__main__":
    main()