########################################################################################################################
#
#   Class name      :   BookStore
#   Description     :   Implement a class with instance variables, a class variable,
#                       constructor to initialize data and increment book count,
#                       and a method to display book details.
#   Input           :   Str, Str
#   Output          :   Void
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1  
    
    def Display(self):
        print(f"{self.Name} by {self.Author}.")
        print(f"No of books : {BookStore.NoOfBooks}")

def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")

    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritche")

    Obj2.Display()

if __name__ == "__main__":
    main()