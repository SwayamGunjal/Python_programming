######################################################################################################
#   Function name   :   NaturalNNumbers()
#   Description     :   Accepts 2 number and prints their arithemetic results.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def NaturalNNumbers(Val):

    for i in range(1,Val+1):
        print(i)

#   Main function
def main():
    No = 0

    No = int(input("Enter Number : "))
    
    NaturalNNumbers(No) 

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