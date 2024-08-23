import csv

def main():

  message = """=======Welcome to Codezilla library=========
  1.View availbale books
  2.Return books
  3.Borrow books
  4.Exit"""

  Book.csv_reader("data_library.csv")

  while True:

    print(message)
    choice = input("Enter your choice: ")
    if choice == "1":

      Book.view_available_books()

    elif choice == "2":
      pass

    elif choice == "3":
      pass
    elif choice == "4":
      break

    else:
      print("Invalid choice")


class Book:
  #library = "Codezilla library"
  all_books = []

  def __init__(self, category, book_name, author, year_of_publication, status,
               number_available):
    self.category = category
    self.book_name = book_name
    self.author = author
    self.year_of_publication = year_of_publication
    self.status = status
    self.copies_number_available = number_available
    Book.all_books.append(self)

  @classmethod
  def csv_reader(cls, file_name):
    with open(file_name) as file:
      csv_reader = csv.DictReader(file)
      for row in csv_reader:
        category = row["Details_Category"]
        book_name = row["Details_Book_Name"]
        author = row["Details_Author"]
        year_of_publication = row["Details_Year_of_Publication"]
        status = row["Status_available"].lower()=="true"
        number_available = int(row["Status_number_available"])
        cls(category, book_name, author, year_of_publication, status,
            number_available)


  
  def __str__(self):
    return f"{self.book_name} is written by {self.author} in {self.year_of_publication}"

  def __repr__(self):
    return f"Book: category = {self.category}, book_name = {self.book_name}, autho r= {self.author}, year_of_publication = {self.year_of_publication}, status = {self.status}, number_available = {self.copies_number_available}"

 
  @classmethod
  def view_available_books(cls):
   for i, book in enumerate(cls.all_books,1): 
     if book.status:
       print(f"{i} - {book.__str__()}\n {book.status}")
     else:
       print(f"{i} - {book.__str__()} ---(Not Available now) \n")
    # sorted(words_summary_lst,
    #  key=lambda word: words_summary_lst.count(word),
    #  reverse=True)



if __name__ == "__main__":
  main()






