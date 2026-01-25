import threading

#########################################################################################################
#   Function name   :   Display1
#   Description     :   Displays numbers from 1 to 50.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def Display1():

    print("1 to 50 :")
    
    for i in range(1,51):
        print(i)
    

#########################################################################################################
#   Function name   :   Display2
#   Description     :   Displays numbers from 50 to 1 in reverse order.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def Display2():

    print("50 to 1 :")

    for i in range(51,1,-1):
        print(i)

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates two threads and ensures sequential execution.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():

    Thread1 = threading.Thread(target=Display1)
    Thread2 = threading.Thread(target=Display2)

    Thread1.start()
    Thread1.join()

    Thread2.start()    
    Thread2.join()

if __name__ == "__main__":
    main()