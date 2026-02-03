########################################################################################################################
#
#   Function name   :   FileCpy
#   Description     :   Copy contents of one file into another file.
#   Input           :   None
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def FileCpy():
    try:
        fobj = open("Demo.txt","r")
        fobj1 = open("ABC.txt","w")

        print("File successfully opened!")

        # File copied
        Data = fobj.read()

        # File overwritten
        fobj1.write(Data)

        fobj1.close()

        # New file read and displayed
        fobj2 = open("ABC.txt","r")
        Data1 = fobj2.read()

        print("Data from destination file is : ")
        print(Data1)

        fobj.close()
        fobj2.close()
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

def main():
    FileCpy()

if __name__ == "__main__":
    main()