######################################################################################################
#   Function name   :   DivisibleByThreeAndFive()
#   Description     :   Accepts 1 number and evaluates if the number is divisible by 3 & 5 or not.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def DivisibleByThreeAndFive(Val):
    if (Val % 3) == 0 and (Val % 5) == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

#   Main function
def main():
    No = int(input("Enter a number : "))
    DivisibleByThreeAndFive(No)   

#   Starter Condition
if __name__ == "__main__":
    main()