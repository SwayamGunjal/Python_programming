########################################################################################################################
#
#   Function name   :   FileExists
#   Description     :   Validates file existence and searches for the given file.
#   Input           :   Str
#   Output          :   Bool
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

import os

def FileExists(FileName):

    Data = os.path.exists(FileName)

    if Data == True:
        return True
    else:
        return False
    

def main():
    Ret = False

    FileName = input("Enter file name : ")

    Ret = FileExists(FileName)
    
    if Ret == True:
        print(f"{FileName} EXISTS!!")
    else:
        print(f"{FileName} does NOT EXIST")

if __name__ == "__main__":
    main()