import datetime
import logging
import sys

logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')


class Library:
    """
         This class is used to keep records of books library.  Created a Library class:
         methods are available in a class:  book_info, add_books, delete_books, issue_books, return_book
         create a main function and run an infinite while loop asking users for their input

    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.book_dict = {}
        for book in list_of_books:
            self.book_dict.update({book: {'lender_name': '', 'lend_date': '', 'status': 'Available'}})

    # book information
    def book_info(self):
        logging.info("We have following books in our library:")
        for book in self.list_of_books:
            print(book)

    # add new book in a list
    def add_books(self, book):
        if book not in self.list_of_books:
            self.list_of_books.append(book)
            logging.info("Book has been added to the book list")
        else:
            logging.warning("Books is already available in the library")

    # delete book from a list
    def delete_books(self, book):
        if book in self.list_of_books:
            self.list_of_books.remove(book)
            logging.info("Book has been deleted to the book list")
        else:
            logging.warning("Book is not available in the library")

    # who owns the book if not present
    def issue_books(self):
        book_name = input("Enter Book Name ").lower()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if book_name in self.book_dict.keys():
            if not self.book_dict[book_name]['status'] == 'Available':
                value = (f"This book is already issued to {self.book_dict[book_name]['lender_name']}"
                         f" on {self.book_dict[book_name]['lend_date']}")
                logging.info(value)

            elif self.book_dict[book_name]['status'] == 'Available':
                book_user = input("Enter Your Name : ")
                self.book_dict[book_name]['lender_name'] = book_user
                self.book_dict[book_name]['lend_date'] = current_date
                self.book_dict[book_name]['status'] = 'Already Issued'
                logging.info("Book Issued Successfully....\n")
        else:
            logging.warning("Book is not available in the library")

    # return the book in a library
    def return_book(self):
        book_name = input("Enter the name of the book you want to return: ")
        if book_name in self.book_dict.keys():
            if self.book_dict[book_name]['status'] == 'Available':
                logging.warning("This book is already available in library. Please check book Name")
                return self.return_books()
            elif not self.book_dict[book_name]['status'] == 'Available':
                self.book_dict[book_name]['lender_name'] = ''
                self.book_dict[book_name]['lend_date'] = ''
                self.book_dict[book_name]['status'] = 'Available'
                logging.info("Successfully Updated\n")
        else:
            logging.error("Book Name Not Found")


if __name__ == "__main__":
    books_name = ['Python', 'Java', 'C++ Basics', 'C#', 'Django']
    library_obj = Library([book.lower() for book in books_name], "The National Library of India")
    while True:
        msg = f"Welcome to the {library_obj.library_name}\nEnter your choice to continue"
        logging.info(msg)
        info = ("1. Book list \n"
                "2. Add book in a list \n"
                "3. Delete book from list \n"
                "4. Issue Book \n"
                "5. Return Book \n"
                "6. quit \n")
        logging.info(info)
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4', '5', '6']:
            logging.warning("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            library_obj.book_info()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to add:")
            library_obj.add_books(book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to delete:")
            library_obj.delete_books(book)

        elif user_choice == 4:
            library_obj.issue_books()

        elif user_choice == 5:
            library_obj.return_book()

        else:
            logging.error("Not a valid option")

        logging.info("Press q to quit and c to continue")

        user_choice_ch = ""
        while user_choice_ch != "c" and user_choice_ch != "q":
            user_choice_ch = input()
            if user_choice_ch == "q":
                sys.exit()
            elif user_choice_ch == "c":
                continue
