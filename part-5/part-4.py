### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
#def new_book():
 #   title = input('Enter Book Title Here: ')
  #  author = input('Enter the Authors name here: ')
  #  year = input('Enter the publication year: ')
  #  rating = input('Enter the average rating of the book: ')
 #   pages = input('Enter how many pages the book has: ')
#
 #   book_dic = {
 #       "title": title,
 #       "author": author,
  #      "year": year,
  #      "rating": rating,
  #      "pages": pages
 #   }

  #  return book_dic

# print(new_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

#def new_book():
 #   title = input('Enter Book Title Here: ')
  #  author = input('Enter the Authors name here: ')
   # year = int(input('Enter the publication year: '))
   # rating = float(input('Enter the average rating of the book: '))
    #pages = int(input('Enter how many pages the book has: '))

    #book_dic = {
     #   "title": title,
      #  "author": author,
       # "year": year,
        #"rating": rating,
        #"pages": pages
    #}

    #return book_dic

#print(new_book())

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def new_book():
 #    title = input('Enter Book Title Here: ')
 #    author = input('Enter the Authors name here: ')
 #    try:
 #        year = int(input('Enter the publication year: '))
 #    except:
 #        year = int(input('Please type a number: '))
 #    try:
 #        rating = float(input('Enter the average rating of the book: '))
#     except:
 #        rating = float(input('Enter a number: '))
 #    try:
#         pages = int(input('Enter how many pages the book has: '))
 #    except:
#         pages = int(input('Try again using whole numbers: '))
#     book_dic = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#
 #    return book_dic

# print(new_book())

### Step 4 - if/elif/else

my_library = [
    {
    "title": "The Dark Tower: The Gunslinger",
    "author": "Stephen King",
    "year": 1982,
    "rating": 4.2,
    "pages": 224
    },
    {
    "title": "The Dark Tower II: The Drawing of the Three",
    "author": "Stephen King",
    "year": 1987,
    "rating": 4.2,
    "pages": 400
    },
    {
    "title": "The Dark Tower III: The Waste Lands",
    "author": "Stephen King",
    "year": 1991,
    "rating": 4.5,
    "pages": 512
    },
    {
    "title": "The Dark Tower IV: Wizard and Glass",
    "author": "Stephen King",
    "year": 1997,
    "rating": 4.5,
    "pages": 787
    },
    {
    "title": "The Dark Tower V: Wolves of the Calla",
    "author": "Stephen King",
    "year": 2003,
    "rating": 4.2,
    "pages": 714
    },
    {
    "title": "The Dark Tower VI: Song of Susannah",
    "author": "Stephen King",
    "year": 2004,
    "rating": 4.2,
    "pages": 432
    },
    {
    "title": "The Dark Tower VII: The Dark Tower",
    "author": "Stephen King",
    "year": 2004,
    "rating": 4.7,
    "pages": 845
    }]

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# 1)__________ back to menu______________
def back_to_menu():
    choice = input('Return to menu? Y or N ')

    if choice.lower() == 'y':
        main_menu()
    else:
        pass

#______________new book function ________________

def new_book():
    title = input('Enter Book Title Here: ')
    author = input('Enter the Authors name here: ')
    try:
        year = int(input('Enter the publication year: '))
    except:
       year = int(input('Please type a number: '))
    try:
      rating = float(input('Enter the average rating of the book: '))
    except:
       rating = float(input('Enter a number: '))
    try:
        pages = int(input('Enter how many pages the book has: '))
    except:
        pages = int(input('Try again using whole numbers: '))
    book_dic = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages}

    my_library.append(book_dic)
    main_menu()

#_________________ print entire library ________________
def print_all_books(list):
    print('These are the books in your library -\n')
    for book in list:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")
    back_to_menu()


#_________________ Search library for title ______________
def search_books(str):
    searched_string = str.lower()
    searched_books = []
    for book in my_library:

        if book["title"].lower().find(searched_string) != -1:
            searched_books.append(book["title"])
            print(book["title"])

    if searched_books == []:
        print("Sorry, it appears that you don't have any books with that search string in the title")
    back_to_menu()


# 0)__________ main menu _______________

def main_menu():

    choice = 5
    while choice > 4 or choice <= 0:
        choice = int(input('Type 1 to add a new book \nType 2 to see a list of all books \nType 3 to search for a book \nType 4 to exit\n'))

        if choice == 1: new_book()
        elif choice == 2: print_all_books(my_library)
        elif choice == 3: search_books(input('Type the name of a book...'))
        else:
            print('Exiting Library')
            pass

if __name__ == '__main__':
    main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

#_____SEE #4 ABOVE__________
