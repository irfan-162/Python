class Library:
    books = []
    @staticmethod
    def addBook(book):
        Library.books.append(book)
    @staticmethod    
    def removeBook(book):
        Library.books.remove(book)
    @staticmethod    
    def displayBooks():
        print("Books in the library:")
        for book in Library.books:
            print(book)        
        

Library.addBook("The Great Gatsby")       
Library.addBook("To Kill a Mockingbird")
Library.addBook("1984")
Library.displayBooks() 
Library.removeBook("1984")
Library.displayBooks()