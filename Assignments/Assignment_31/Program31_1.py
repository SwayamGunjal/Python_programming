########################################################################################################################
#
#   Function name   :   DirectoryScanner
#   Description     :   Accepts directory name and file extension from user and displays all matching files.
#   Input           :   String, String
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   05/02/2026
#
########################################################################################################################

import sys
import os

def DirectoryScanner(DirName, Extension):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("There is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            if(fname.endswith(Extension)):
                print(fname)

def main():
    Border = "-"*50
    print(Border)

    print("--------- Marvellous Directory Automation --------")

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : Application_Name Directory_Name Extension")
        return

    DirectoryScanner(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
