########################################################################################################################
#
#   Function name   :   SearchWord
#   Description     :   Returns true if given word is present in the text file and vice versa.
#   Input           :   Str
#   Output          :   Bool
#   Author          :   Swayam Satish Gunjal
#   Date            :   03/02/2026
#
########################################################################################################################

def SearchWord(name):
    try:
        fobj = open("ABC.txt","r")

        Data = fobj.read()

        if Data.__contains__(name):
            return True
        else:
            return False
    
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")

def main():
    Ret = False

    name = input("Enter a word : ")

    Ret = SearchWord(name)
    
    if Ret == True:
        print(f"{name} is PRESENT in the file")
    else:
        print(f"{name} is NOT PRESENT in the file")

if __name__ == "__main__":
    main()