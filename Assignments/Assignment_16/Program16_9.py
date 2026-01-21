#########################################################################################################
#   Function name   :   main
#   Description     :   Prints first 10 even numbers.
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

#   Main function
def main(): 

    for i in range(2, 21, 2):
        print(i)

#   Starter Condition
if __name__ == "__main__":
    main()



# Alternate version :

# def main(): 

#     for i in range(2, 21):
#         if ((i % 2) == 0):
#             print(i)
