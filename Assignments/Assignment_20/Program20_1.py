import threading

#########################################################################################################
#   Function name   :   EvenNum
#   Description     :   Prints the first 10 even numbers.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def EvenNum():
    
    print("Even :")

    for i in range(2, 21, 2):
        print(i)

#########################################################################################################
#   Function name   :   OddNum
#   Description     :   Prints the first 10 odd numbers.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def OddNum():

    print("Odd :")
    
    for j in range(1, 22, 2):
        print(j)

#########################################################################################################   
#   Function name   :   main
#   Description     :   Creates two threads to execute EvenNum() and OddNum() functions.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

def main():
    
    Even = threading.Thread(target=EvenNum)
    Odd = threading.Thread(target=OddNum)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()