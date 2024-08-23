#project1#################################
#Make a program that reads the data of each the
# following books summaries files:
# Atomic Habits, Deep Work and Dopamine Nation
# then save the data of each file in a new file but in
# reverse order and make all the letters upper case.


def read_modify_books(book_file, str_name="modified_book"):
  try:
    with open(book_file) as f:
      new_book_file = f.read()

    with open(str_name, "w") as f:
      f.write(new_book_file[::-1].upper())
  #errors
  #No Such File Or Directory
  # Not Readable
  # Not Writable
  except OSError as error:
    print(error)


read_modify_books("atomic_habits_summary.txt", "new_atomic_habits")

#project2##############################33
#Add all the books summaries files to one text file
# and make sure to add the book name before the text
# of each summary
# All the files should be in one folder which is
# books_summaries that you will read all the files
# from it
# The code will be in the same folder as the
# books_summaries folder


def add_summary(books_file_lst):
  try:
    for book in books_file_lst:
      with open(book) as f:
        summary = f.read()
      with open("all_book_summaries", "a") as f:
        f.write(f"\n{'*'*70} {book}\n{'-'*30}\n{summary}")
  #errors
  #No Such File Or Directory
  # Not Readable
  # Not Writable
  except OSError as error:
    print(error)


books_file_lst = [
  "atomic_habits_summary.txt", "the_power_of_habits_summary.txt",
  "so_good_to_ignore_summary.txt", "deep_work_summary.txt",
  "dopamine_nation_summary.txt", "the_lady_tasting_tea_summary.txt"
]
add_summary(books_file_lst)
