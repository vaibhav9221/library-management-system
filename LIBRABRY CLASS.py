# MADE A LIBRARY CLASS
class Library:
    #LIST OF BOOKS, NAME OF LIBRARY
    def __init__(self,list,name):
        self.list=list
        self.name=name
        self.lendDic = {}
    #DISPLAY BOOK
    def displayBooks(self):
        print(f"we have following book in our library :{self.name}")
        for book in self.list:
            print(book)
    # LEND BOOK BY USER

    def lendBooks(self,user,book):
        if book not in self.lendDic.keys():
            self.lendDic.update({book:user})
            print("Lender book data base is updated .u can take the book now.")
        else:
            print(f"Book is already used by {self.lendDic[book]}")
    #NEW BOOK ADDED IN THE LIST
    def addBook(self,book):
        self.list.append(book)
        print("Book has been Added  to the library")
    #RETURN ANY LENDED BOOKS
    def returnBook(self,book):
        self.lendDic.pop(book)

if __name__ == '__main__':
    vaibhav=Library(['python','data structure','half girlfriend','fundamentals of c'],"VAIBHAV")
    while (True):
        print(f"WELCOME TO THE {vaibhav.name} Library ")
        print("enter you choice to continue")
        print('1.Display book')
        print('2.Lend book')
        print('3.Add book')
        print('4.Return book')

        choice=input()

        if   choice not in ['1','2','3','4']:
            continue
        else:
            choice=int(choice)
        if choice==1:
            vaibhav.displayBooks()
        elif choice ==2:
            book=input("Enter the book u want to lend:")
            user=input("Enter your name:")
            vaibhav.lendBooks(user,book)
        elif choice ==3:
            book=input("Enter a book u want to add")
            vaibhav.addBook(book)
        elif choice==4:
            book = input("Enter a book u want to return")
            vaibhav.returnBook(book)
        else:
            print("enter a valid option")

        print("Press Q to quit and C to continue")
        user_choice = input()
        while(user_choice=="C" and user_choice=="Q"):
         #   user_choice=input()
            if user_choice=="Q":
                exit()
            elif user_choice=="C":
                continue



