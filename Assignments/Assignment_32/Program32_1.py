########################################################################################################################
#
#   Function name   :   DirectoryChecksum
#   Description     :   Accepts directory name and displays checksum of all files.
#   Input           :   String
#   Output          :   None
#   Author          :   Swayam Satish Gunjal
#   Date            :   06/02/2026
#
########################################################################################################################

import sys
import os
import hashlib

def DirectoryChecksum(DirName):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            FilePath = os.path.join(FolderName, fname)

            fd = open(FilePath, 'rb')
            Data = fd.read()
            fd.close()

            HashObj = hashlib.md5()
            HashObj.update(Data)

            print(fname, ":", HashObj.hexdigest())

def main():
    Border = "-" * 50
    print(Border)
    print("--------- Marvellous Directory Automation --------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage : Application_Name Directory_Name")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()
