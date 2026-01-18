######################################################################################################
#   Function name   :   ChkVowel()
#   Description     :   Accepts 1 number and checks if it is a Vowel or not.
#   Input           :   Str
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def ChkVowel(Val):

    if (Val == 'a' or Val == 'e' or Val == 'i' or Val == 'o' or Val == 'u') or (Val == 'A' or Val == 'E' or Val == 'I' or Val == 'O' or Val == 'U'):
        return True
    else:
        return False

#   Main function
def main():
    Letter = input("Enter a character : ")
    Ret = ChkVowel(Letter)

    if (Ret == True):
        print(Letter,"is a Vowel")
    else:    
        print(Letter,"is not a Vowel") 

#   Starter Condition
if __name__ == "__main__":
    main()