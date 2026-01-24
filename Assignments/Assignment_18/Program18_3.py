#########################################################################################################
#   Function name   :   MinElement
#   Description     :   Returns the smallest element in the list. 
#   Input           :   List
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def MinElement(Data):
    Min = Data[0]
    
    for i in Data:
        if i < Min:
            Min = i

    return Min
    

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


    Ret = MinElement(Data)
    
    print("Min : ",Ret)

#   Starter Condition
if __name__ == "__main__":
    main()