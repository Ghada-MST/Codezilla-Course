#project1#####################################################
countries_and_capitals = [
("Afghanistan", "Kabul"),
("Albania", "Tirana"),
("Algeria", "Algiers"),
("Andorra", "Andorra la Vella"),
("Angola", "Luanda"),
("Antigua and Barbuda", "Saint John's"),
("Argentina", "Buenos Aires"),
("Armenia", "Yerevan"),
("Australia", "Canberra"),
("Austria", "Vienna"),
("Azerbaijan", "Baku"),
("Bahamas", "Nassau"),
("Bahrain", "Manama"),
("Bangladesh", "Dhaka")]

for index, (country, cpital) in enumerate(countries_and_capitals,1):
  print(f'{index}. {country}: {cpital}')


#project2#####################################################

sentences = ['Hello from Codezilla', 'Python Course is awesome', 'I enjoy learning Python with Codezilla']


for index, sentence in enumerate(sentences):
  sentences[index] = sentences[index].upper().replace(' ','-') 
print(sentences)

#project3#####################################################

books = [
("The 7 Habits of Highly Effective People", "Stephen R. Covey"),
("How to Win Friends and Influence People", "Dale Carnegie"),
("Atomic Habits", "James Clear"),
("The 4-Hour Work Week", "Tim Ferriss"),
("Deep Work", "Cal Newport"),
("So Good They Can't Ignore You", "Cal Newport"),
("Digital Minimalism", "Cal Newport"),]

for index, (book,author) in enumerate(books):
  print(f'{index+1}. Book: {book} - Author: {author}')

#method 2 حل مهندس اسلام
#Loop through the list of books and authors using enumerate
for i, book in enumerate(books):
  # Print the book and author
  print(f"{i + 1}. Book: {book[0]} - Author: {book[1]}")