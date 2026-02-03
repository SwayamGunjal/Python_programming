########################################################################################################################
#
#   Function name   :   FileCompare
#   Description     :   Compares file contents of 2 given files for either individuality or identicality.
#   Input           :   Str
#   Output          :   Bool
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def FileCompare(FileName1, FileName2):
    try:
        fobj1 = open(FileName1,"r")
        fobj2 = open(FileName2,"r")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        fobj1.close()
        fobj2.close()
        
        if Data1 == Data2:
            return True
        else:
            return False
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

def main():
    Ret = False

    FileName1 = input("Enter the first file name : ")
    FileName2 = input("Enter the second file name : ")
    
    Ret = FileCompare(FileName1, FileName2)

    if Ret == True:
        print("SUCCESS (Both files have identical data)")
    else:
        print("FAILURE (Both files DO NOT have identical data)")

if __name__ == "__main__":
    main()