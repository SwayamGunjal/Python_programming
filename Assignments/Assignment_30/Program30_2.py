########################################################################################################################
#
#   Function name   :   WordCount
#   Description     :   Count number of words in a text file.
#   Input           :   None
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def WordCount():
    try:
        Count = 0
        fobj = open("Demo.txt","r")
        print("File successfully opened!")

        Data = fobj.read()

        if Data != "": 
            for i in Data:
                if ((i == " ") or (i == "\n")):
                    Count += 1
            Count +=1

        print("Data from file is : ")
        print(Data)

        fobj.close()

        return Count
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        return 0

def main():
    Ret = WordCount()
    print("Word count : ", Ret)

if __name__ == "__main__":
    main()