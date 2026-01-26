import threading

def ChkPrime(No):
    if No <= 1:
        return False
    
    for i in range(2, No):
        if ((No % i) == 0):
            return False
    return True

#########################################################################################################
#   Function name   :   
#   Description     :   
#   Input           :   
#   Output          :   
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def PrimeNum(Data):

    Dummy1 = list()

    print("Prime : ")
    
    for i in Data:
        if ChkPrime(i):
            Dummy1.append(i)
    
    print(Dummy1)
    

#########################################################################################################
#   Function name   :   
#   Description     :   
#   Input           :   
#   Output          :   
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def NonPrimeNum(Data):

    Dummy2 = list()

    print("Non-Prime : ")
    
    for i in Data:
        if ChkPrime(i) == False:
            Dummy2.append(i)
    
    print(Dummy2)
    

#########################################################################################################
#   Function name   :   
#   Description     :   
#   Input           :   
#   Output          :   
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():

    Data = list()

    Size = int(input("Enter list size :"))

    print("Enter elements : ")

    for i in range(Size):
        Data.append(int(input()))

    Prime = threading.Thread(target=PrimeNum, args=(Data,))
    NonPrime = threading.Thread(target=NonPrimeNum, args=(Data,))

    Prime.start()
    Prime.join()

    NonPrime.start()    
    NonPrime.join()

if __name__ == "__main__":
    main()