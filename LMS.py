import datetime
import os

class LMS:
     """This class is used to keep record of books in library
     It has four module i.e. "Display Books", "Issue Books", "Return Books", "Add Books" """
     def __init__(self, list_of_books, library_name):
          self.list_of_books = list_of_books
          self.library_name = library_name
          self.book_dict ={}
          book_ID = 19980
          #how to read notepad file
          with open(self.list_of_books) as book:
               lines = book.readlines()
               #how to read each line: apply loop
          for line in lines: 
               #update books dictionary
               self.book_dict.update({str(book_ID):{"books_title":line.replace("\n", ""), "lender_name":""
               , "Issue_Date": "", "Status": "Available"}})
               book_ID += 1

     def displayBooks(self):
          print("-------------------Book List-------------------")
          print("Book ID", "\t", "Title")
          print()
          for key, value in self.book_dict.items():

               print(key,"\t\t", value.get("books_title"),"-[",value.get("Status"),"]") #value.get helps to get the keys value
               
     def Issue_books(self):
          books_id = input("Enter books ID: ")
          current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          if books_id in self.book_dict.keys():
              if self.book_dict[books_id]['Status'] == "Already Issued":
                  print(f"This book is already issued to {self.book_dict[books_id]['lender_name']} "
                        f"on {self.book_dict[books_id]['Issue_date']}")
                  return self.Issue_books()
              elif self.book_dict[books_id]['Status'] == "Available":
                  yourname = input("Enter your name: ")
                  self.book_dict[books_id]['lender_name'] = yourname
                  self.book_dict[books_id]['Issue_date'] = current_date
                  self.book_dict[books_id]['Status'] = 'Already Issued'
                  print("Book Issued Successfully")
              else:
                  print("Book ID not found")
                  return self.Issue_books()
          else:
               print("Book ID not found")
       
     def addbooks(self):
          new_books = input("Enter the book title: ")
          if new_books == "":
               return self.addbooks()
          else:
               with open(self.list_of_books, "a") as bk:
                    bk.writelines(f"{new_books}\n")
                    self.book_dict.update({str(int(max(self.book_dict))+1):{"books_title":new_books,
                    "lender_name":"", "Issue_date":"", "Status":"Available"}})
                    print(f"This books '{new_books}' has been added successfully")

     def return_books(self):
          books_id = input("Enter book ID: ")
          if books_id in self.book_dict.keys():
              if not self.book_dict[books_id]["Status"] == "Available":
                  print(f"Returning book '{self.book_dict[books_id]['books_title']}'")
                  self.book_dict[books_id]["lender_name"] = ""
                  self.book_dict[books_id]["Issue_date"] = ""
                  self.book_dict[books_id]["Status"] = "Available"
                  print("Book returned successfully")
              else:
                  print("This book is already available in the library. Please check your ID.")
                  return self.return_books()
          else:
              print("Book ID not found")

try:
     myLMS = LMS("LMS.txt", "Atled EBook ")
     press_key_list = {"D": "Display Books", "I":"Issue Books", "A": "Add Books",
                        "R": "Return Books", "Q": "Quit"}    
     key_press = False 
     while True:    
          print(f"\n Welcome to {myLMS.library_name}\n")   
          for key, value in press_key_list.items():
               print(f"'Press', {key} 'To', {value}")
          key_press=input("Press key: ").lower()
          if key_press == "i":
               print("\nCurrent Selection:Issue Books\n")
               myLMS.Issue_books()
          elif key_press == "a":
               print("\nCurrent Selection:Add Books\n")
               myLMS.addbooks()
          elif key_press == "d":
               print("\nCurrent Selection:Display Books\n")
               myLMS.displayBooks()
          elif key_press == "r":
               print("\nCurrent Selection:Return Books\n")
               myLMS.return_books()
          elif key_press == "q":
               break
          else:
               continue
except Exception as e:
     print("Something went wrong. Please check your input")

                   
                   

    