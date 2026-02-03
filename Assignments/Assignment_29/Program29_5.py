########################################################################################################################
#
#   Function name   :   WordFreq
#   Description     :   Counts frequency of a given string in a file.
#   Input           :   Str, Str
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def WordFreq(FileName, Term):
    try:
        Count = 0

        fobj = open(FileName,"r")

        Data = fobj.read()

        Count = Data.count(Term)
        
        fobj.close()
        return Count

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        return 0


def main():
    Ret = 0

    FileName = input("Enter file name : ")
    Term = input("Enter one string : ")
    
    Ret = WordFreq(FileName, Term)

    print("String frequency : ",Ret)    

if __name__ == "__main__":
    main()