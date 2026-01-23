#########################################################################################################
#   Function name   :   StrLen
#   Description     :   Calculates and prints the length of the input string.
#   Input           :   Str
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

def StrLen(Val):
    Count = 0

    for i in Val:
        Count += 1

    return Count

#   Main function
def main(): 
    
    Ret = 0

    Name = input("Enter name : ")

    Ret = StrLen(Name)

    print(Ret)
    

#   Starter Condition
if __name__ == "__main__":
    main()



# Alternate version :

# def main(): 

#     Count = 0

#     Name = input("Enter name : ")

#     Count = len(Name)

#     print(Count)
