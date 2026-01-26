import threading

#########################################################################################################
#   Function name   :   MaxElement
#   Description     :   Finds and displays the maximum element from the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def MaxElement(Data):
    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i

    print("Maximum value : ",Max) 
    
    

#########################################################################################################
#   Function name   :   MinElement
#   Description     :   Finds and displays the minimum element from the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def MinElement(Data):
    Min = Data[0]
    for i in Data:
        if i < Min:
            Min = i

    print("Minimum value : ",Min) 
    
    

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates threads to display maximum and minimum elements of a list.
#   Input           :   Integer, List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():

    Data = list()

    Size = int(input("Enter list size :"))

    print("Enter elements : ")

    for i in range(Size):
        Data.append(int(input()))

    Thread1 = threading.Thread(target=MaxElement, args=(Data,))
    Thread2 = threading.Thread(target=MinElement, args=(Data,))

    Thread1.start()
    Thread1.join()

    Thread2.start()    
    Thread2.join()

if __name__ == "__main__":
    main()