#########################################################################################################
#   Function name   :   FirstEven
#   Description     :   Prints first 10 even numbers.
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

def FirstEven():
    for i in range(2, 21, 2):
        print(i)

#   Main function
def main(): 

    FirstEven()

#   Starter Condition
if __name__ == "__main__":
    main()



# Alternate version :

# def main(): 

#     for i in range(2, 21):
#         if ((i % 2) == 0):
#             print(i)
