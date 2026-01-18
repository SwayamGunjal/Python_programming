######################################################################################################
#   Function name   :   arithmetic()
#   Description     :   Accepts 2 number and prints their arithemetic results.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def arithmetic(Val1, Val2):

    print("Addition : ",Val1 + Val2)
    print("Substraction : ",Val1 - Val2)
    print("Multiplication : ",Val1 * Val2)
    print("Division : ",Val1 / Val2)

#   Main function
def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first Number : "))
    No2 = int(input("Enter second Number : "))
    
    arithmetic(No1,No2) 

#   Starter Condition
if __name__ == "__main__":
    main()



#    Main function
# def main():
#     No1 = 0
#     No2 = 0

#     No1 = int(input("Enter first Number : "))
#     No2 = int(input("Enter second Number : "))

#     print("Addition : ",No1 + No2)
#     print("Substraction : ",No1 - No2)
#     print("Multiplication : ",No1 * No2)
#     print("Division : ",No1 / No2)

#   Starter Condition
# if __name__ == "__main__":
#     main()