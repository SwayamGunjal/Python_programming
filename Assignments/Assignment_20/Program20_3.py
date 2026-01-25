import threading

#########################################################################################################
#   Function name   :   EvenSum
#   Description     :   Calculates and prints the sum of even elements from the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def EvenSum(No):
    Sum = 0

    for i in No:
        if ((i % 2) == 0):
            Sum = Sum + i
    
    print("Sum of Even elements : ",Sum)

#########################################################################################################
#   Function name   :   OddSum
#   Description     :   Calculates and prints the sum of odd elements from the list.
#   Input           :   List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def OddSum(No):
    Sum = 0

    for i in No:
        if ((i % 2) != 0):
            Sum = Sum + i
    
    print("Sum of Odd elements : ",Sum)

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates two threads to calculate sum of even and odd elements of a list.
#   Input           :   Integer, List
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():
    Size = 0
    Data = list()

    print("Enter size of list : ")
    Size = int(input())

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    EvenList = threading.Thread(target=EvenSum, args=(Data,))
    OddList = threading.Thread(target=OddSum, args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()