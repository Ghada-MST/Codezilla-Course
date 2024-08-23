import string


def main():
  books_summary = read_txt_file("books_summaries.txt")

  modified_books_summary = lower_case_no_punctuation(books_summary)

  sorted_words = sort_word_summary(modified_books_summary)

  sorted_letters = sort_letter_summary(modified_books_summary)

  occurrence_letters = occurrence_element(sorted_letters)

  occurrence_words = occurrence_element(sorted_words)

  save_to_file(occurrence_words, "books_summary_words")

  save_to_file(occurrence_letters, "books_summary_letters")


def read_txt_file(txt_file):
  """Get text file
    Read the text file

    Parameter: text file

    Return: variable books_summary with the readed txt file"""

  with open("books_summaries.txt") as f:
    books_summary = f.read()
  return books_summary


def lower_case_no_punctuation(books_summary):
  """Get the variable of readed txt file
  Convert all txt to lower case
  Replace all new lines with empty strings
  Remove all the punctuations
  join all the txt again 

  Parameter: variable of txt file

  Return: Modified txt"""

  books_summary_lower = books_summary.lower().replace("\n", "")

  without_punctutation = [
    letter for letter in books_summary_lower
    if letter not in string.punctuation
  ]
  modified_books_summary = ''.join(without_punctutation)
  return modified_books_summary


def sort_letter_summary(modified_books_summary):
  """Get the modified txt
  make a list of letters
  remove numbers and -
  sort the letters aphabetically

  Parameter: modified txt

  Return: sorted letters list"""
  letters_summary_lst = [
    letter for letter in modified_books_summary if letter.isalpha()
  ]

  sorted_letter_lst = sorted(letters_summary_lst)
  return sorted_letter_lst


def sort_word_summary(modified_books_summary):
  """Get the modified txt
    make a list of words
    Sort the words by frequency (the most repeated words first) 

    Parameter: modified txt

    Return: sorted word list"""

  words_summary_lst = modified_books_summary.split(" ")

  sorted_word_lst = sorted(words_summary_lst,
                           key=lambda word: words_summary_lst.count(word),
                           reverse=True)
  return sorted_word_lst


def occurrence_element(sorted_list):
  """Get the sorted_list

    Parameter: sorted_list

    Return: dictionary for items occurence in list """

  occurrence = {item: sorted_list.count(item) for item in sorted_list}
  return occurrence


def save_to_file(occurrence_dict, new_file):
  """Get occurrence_dictionary
    Save the occurrence dictionaries words or letters in a file

    parameter: occurrence_dictionary of letters or words, the name of the new file

    Return: txt file created
    """
  with open(new_file, 'w') as f:

    for element, occurrence in occurrence_dict.items():

      f.write(f'{element.title()} : {occurrence}\n')


if __name__ == "__main__":
  main()
