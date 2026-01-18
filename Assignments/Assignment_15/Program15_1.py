#########################################################################################################
#   LambdaFn name   :   Square
#   CoreFn used     :   map()
#   Description     :   Accepts list data and converts each element into square.
#   Input           :   List
#   Output          :   List
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

Square = lambda No : No ** 2

#   Main function
def main(): 
    
    Data = [2,4,6,8,10]

    MData = list(map(Square,Data))

    print(MData)


#   Starter Condition
if __name__ == "__main__":
    main()
