########################################################################################################################
#
#   Function name   :   ReadLine
#   Description     :   Reads the text file line by line.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def ReadLine():
    try:
        Count = 0
        fobj = open("Demo.txt","r")
        print("File successfully opened!")

        for line in fobj:
            print(line, end="")

        fobj.close()
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")


def main():
    ReadLine()

if __name__ == "__main__":
    main()