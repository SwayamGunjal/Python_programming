import sys

def main():
    Border = "-"*40
    print(Border)
    Border = "--------- Marvellous Automation --------"
    print(Border)
    Border = "-"*40
    print(Border)
    print()
    
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform ____")
            print("This is a Automation Script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ____________")
            print("Argument2 : ____________")

        else:
            print("Use the given flags as : ")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")

    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as : ")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")
    
    print()
    print(Border)
    Border = "---  Thank you for using our script ----"
    print(Border)
    Border = "------- Marvellous Infosystems ---------"
    print(Border)

if __name__ == "__main__":
    main()