import threading

#########################################################################################################
#   Function name   :   ElementSum
#   Description     :   Calculates and displays the sum of all elements in the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   26/01/26
#########################################################################################################

def ElementSum(Data):
    Sum = 0
    for i in Data:
        Sum = Sum + i

    print("Sum of elements : ",Sum) 
    
    

#########################################################################################################
#   Function name   :   ElementProd
#   Description     :   Calculates and displays the product of all elements in the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   26/01/26
#########################################################################################################

def ElementProd(Data):
    Prod = 1
    for i in Data:
        Prod = Prod * i

    print("Product of elements : ",Prod) 
    
    

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates threads to calculate sum and product of list elements.
#   Input           :   Integer, List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   26/01/26
#########################################################################################################

def main():

    Data = list()

    Size = int(input("Enter list size :"))

    print("Enter elements : ")

    for i in range(Size):
        Data.append(int(input()))

    Thread1 = threading.Thread(target=ElementSum, args=(Data,))
    Thread2 = threading.Thread(target=ElementProd, args=(Data,))

    Thread1.start()
    Thread1.join()

    Thread2.start()    
    Thread2.join()

if __name__ == "__main__":
    main()