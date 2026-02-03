########################################################################################################################
#
#   Function name   :   FileRead
#   Description     :   Reads the text file line by line.
#   Input           :   Str
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def FileRead(FileName):
    try:
        Count = 0
        fobj = open(FileName,"r")
        print("File successfully opened!")

        for line in fobj:
            print(line, end="")

        fobj.close()
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")


def main():
    FileName = input("Enter file name : ")
    FileRead(FileName)

if __name__ == "__main__":
    main()