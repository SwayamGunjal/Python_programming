######################################################################################################
#   Function name   :   ChkVowel()
#   Description     :   Accepts 1 number and checks if it is a Vowel or not.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def PrintFactor(Val):

    for i in range(1,Val+1):
        if (Val % i) == 0:
            print(i)

#   Main function
def main():
    No = 0

    No = int(input("Enter a Number : "))
    PrintFactor(No) 

#   Starter Condition
if __name__ == "__main__":
    main()