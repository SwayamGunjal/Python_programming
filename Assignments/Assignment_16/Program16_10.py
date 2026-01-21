#########################################################################################################
#   Function name   :   main
#   Description     :   Calculates and prints the length of the input string.
#   Input           :   Str
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

#   Main function
def main(): 
    
    Count = 0

    Name = input("Enter name : ")

    for i in Name:
        Count += 1

    print(Count)
    

#   Starter Condition
if __name__ == "__main__":
    main()



# Alternate version :

# def main(): 

#     Count = 0

#     Name = input("Enter name : ")

#     Count = len(Name)

#     print(Count)
