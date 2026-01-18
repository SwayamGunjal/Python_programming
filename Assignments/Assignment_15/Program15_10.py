#########################################################################################################
#   LambdaFn name   :   CountEven
#   CoreFn used     :   filter()
#   Description     :   Accepts list data and returns count of even elements within the list.
#   Input           :   List[int]
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

CountEven = lambda No : (No % 2 == 0)

#   Main function
def main(): 
    
    Data = [1,2,3,4,6,8,10]

    FData = len(list(filter(CountEven,Data)))

    print(FData)


#   Starter Condition
if __name__ == "__main__":
    main()
