##############################################################################################################
#   File name       :   MarvellousNum.py
#   Description     :   A user-defined module that contains a function "ChkPrime" which checks whether 
#                       numbers are prime or not.
#   Input           :   List
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
##############################################################################################################

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True
