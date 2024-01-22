# Let's assign variables to represent a book you enjoy.

# Step 2 - Strings
# Let's start with Python strings. Replace the "None" with the name of a book, and below the name of the author of your book.

book_name = "Merlin"
author = "Mary Stewart"
# book_name = "Dune"
# author = "Frank Herbert"


# Step 3 - Concatenation and f-strings
# Use concatenation and f-strings to make a sentence about your author and book name.


sentence1 = book_name + ' is historical fiction written by ' + author
# sentence1 = book_name + " is written by " + author + "."
sentence2 = f'{author}, penned the Arthurian legend, titled: {book_name}.'
# sentence2 = f"Author, {author}, wrote the book {book_name}."


# Step 4 - Integers
# Now let's practice Integers. Replace the "None" below with the publication date of your book.
publication_year = 1980
# publication_year = 1965


# Step 5 - Floats
# Now estimate what the retail value of your book would be at a store and replace the "None" below with a float value of the price. (Doesn't have to be accurate.)
book_price = 8.99
# book_price = 17.99


# Step 6 - Booleans
# Now we will practice with booleans. Replace the "is_awesome" variable with a boolean. True if your book is awesome, False if your book is not awesome.
is_awesome = True
# is_awesome = True


# Step 7 - print and type functions
# Follow the instructions, and below this line, code all of the suggested print statements and the type statements.
# Code below

print('Book Name: ' +book_name)
print('Author: ' +author)
print(f'It was published in {publication_year}')
print(f'You can purchase it for {book_price}')
print(sentence1)
print(sentence2)
print(f'The book is awesome? {is_awesome}')

print(type(book_name))
print(type(author))
print(type(publication_year))
print(type(book_price))
print(type(sentence1))
print(type(sentence2))
print(type(is_awesome))
