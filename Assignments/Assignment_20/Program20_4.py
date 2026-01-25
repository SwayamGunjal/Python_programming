import threading

#########################################################################################################
#   Function name   :   LowerCnt
#   Description     :   Counts and prints the number of lowercase letters in the string.
#   Input           :   Str
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def LowerCnt(name):
    
    print("LowerCnt TID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    Count = 0

    for i in name:
        if ('a' <= i <= 'z'):
            Count = Count + 1
    
    print("Count of Lowercase letters : ",Count)

#########################################################################################################
#   Function name   :   UpperCnt
#   Description     :   Counts and prints the number of uppercase letters in the string.
#   Input           :   Str
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def UpperCnt(name):

    print("UpperCnt TID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    Count = 0

    for i in name:
        if  ('A' <= i <= 'Z'):
            Count = Count + 1
    
    print("Count of Uppercase letters : ",Count)

#########################################################################################################
#   Function name   :   DigiCnt
#   Description     :   Counts and prints the number of digits in the string.
#   Input           :   Str
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def DigiCnt(name):

    print("DigiCnt TID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    Count = 0

    for i in name:
        if ('0' <= i <= '9'):
            Count = Count + 1
    
    print("Count of Digits : ",Count)

#########################################################################################################
#   Function name   :   main
#   Description     :   Creates three threads to count lowercase, uppercase, and digit characters.
#   Input           :   Str
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   25/01/26
#########################################################################################################

def main():
    
    print("Enter a string : ")
    Data = input()

    Small = threading.Thread(target=LowerCnt, args=(Data,))
    Capital = threading.Thread(target=UpperCnt, args=(Data,))
    Digits = threading.Thread(target=DigiCnt, args=(Data,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()


if __name__ == "__main__":
    main()