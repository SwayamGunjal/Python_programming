#########################################################################################################
#   LambdaFn name   :   Filter, Map, Reduce
#   CoreFn          :   filter(), map(), reduce()
#   Description     :   Filters elements between 70 and 90, increments each by 10, and returns the product.
#   Input           :   List
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

from functools import reduce

#   Main function
def main(): 
    
    Size = 0
    Data = list()

    Size = int(input("Enter size of list :"))

    for i in range(Size):
        Data.append(int(input()))

    print("Input list = ", Data)
    
    FData = list(filter(lambda Data : Data >= 70 and Data <= 90,Data))
    print("List after filter = ",FData)

    MData = list(map(lambda Data : Data + 10,FData))
    print("List after map = ",MData)

    RData = reduce(lambda A, B: A * B ,MData)
    print("Output after reduce = ",RData)



#   Starter Condition
if __name__ == "__main__":
    main()
