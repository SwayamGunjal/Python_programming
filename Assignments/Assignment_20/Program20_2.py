import threading

#########################################################################################################
#   Function name   :   EvenFact
#   Description     :   Calculates and prints the sum of even factors of a given number.
#   Input           :   Integer
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def EvenFact(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        if ((No % i) == 0):
            Sum = Sum + i
    
    print("Sum of Even Factors : ",Sum)

#########################################################################################################
#   Function name   :   OddFact
#   Description     :   Calculates and prints the sum of odd factors of a given number.
#   Input           :   Integer
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def OddFact(No):
    Sum = 0

    for i in range(1, No + 1, 2):
        if ((No % i) == 0):
            Sum = Sum + i
    
    print("Sum of Odd Factors : ",Sum)

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates two threads to compute even and odd factors of a number.
#   Input           :   Integer
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():
    
    print("Enter a number : ")
    Val = int(input())

    EvenFactor = threading.Thread(target=EvenFact, args=(Val,))
    OddFactor = threading.Thread(target=OddFact, args=(Val,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

if __name__ == "__main__":
    main()