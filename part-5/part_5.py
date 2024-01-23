### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

library = "library.txt"
# Code here
#def new_book():
#    title = input('Enter Book Title Here: ')
#    author = input('Enter the Authors name here: ')
 #   try:
#        year = int(input('Enter the publication year: '))
 #   except:
 #      year = int(input('Please type a number: '))
 #   try:
#      rating = float(input('Enter the average rating of the book: '))
#    except:
#       rating = float(input('Enter a number: '))
#    try:
#        pages = int(input('Enter how many pages the book has: '))
#    except:
 #       pages = int(input('Try again using whole numbers: '))
 #   book_dic = {
 #       "title": title,
 #       "author": author,
 #       "year": year,
 #       "rating": rating,
 #       "pages": pages}
#
 #   with open(library, "a") as f:
 #       f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# new_book()
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

#def print_all_books():
#    print('These are the books in your library -\n')
#
#    with open("library.txt", "r") as f:
#        file = f.readlines()
#
#        for line in file:
#            title, author, year, rating, pages = line.split(", ")
#
#            print(f"Title: {title}, Author: {author}, Year: {year}, Rating:
#            {rating}, Pages: {pages}")


#print_all_books()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def back_to_menu():

    choice = input('Return to menu? Y or N ')

    if choice.lower() == 'y':
        main_menu(library)
    elif choice.lower() == 'n':
        pass
    else:
        back_to_menu()

#______________new book function ________________

def new_book(library):
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

    with open(library, "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
    main_menu(library)

#_________________ print entire library ________________
def print_all_books(library):
    print('These are the books in your library -\n')

    for book in book_dic(library):
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")
    back_to_menu()


#_________________ Search library for title ______________?????
def search_books(str, library):
    searched_string = str.lower()
    searched_books = []
    for book in library:

        if book["title"].lower().find(searched_string) != -1:
            searched_books.append(book["title"])
            print(book["title"])

    if searched_books == []:
        print("Sorry, it appears that you don't have any books with that search string in the title")
    back_to_menu()

#________________view highest rated book in collection_________________

def highest_rated(library):
    highest = 0
    novel = ''
    for books in book_dic(library):
        if books['rating'] > highest:
            highest = books['rating']
            novel = books['title']
        else:
            continue
    print(novel)
    back_to_menu()

#____________________view which book takes the longest to read______________
def longest_read(library):
    longest = 0
    novel = ''
    for books in book_dic(library):
        if books['pages'] > longest:
            longest = books['pages']
            novel = books['title']
    print(novel)
    back_to_menu()

#______________show which author's books you own the most of_________________

def favorite_author(library):

    author_dic = {}
    for book in book_dic(library):
        author_name = book['author']
        if book['author'] in author_dic:
            author_dic[author_name] += 1
        else:
            author_dic[author_name] = 1
    print(max(author_dic.items(), key=lambda x:x[1])[0])
    back_to_menu()

def book_dic(library):
    books_list = []
    with open(library, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

# 0)__________ main menu _______________

def main_menu(library):

    choice = 9
    while choice > 8 or choice <= 0:
        choice = int(input('Type 1 to add a new book \nType 2 to see a list of all books \nType 3 to search for a book \nType 4 for a running total of books in your library \nType 5 to see the highest rated book in your collection \nType 6 to see which book takes the longest to read \nType 7 to see which Author book you have the most of \nType 8 to exit\n'))

        if choice == 1: new_book(library)
        elif choice == 2: print_all_books(library)
        elif choice == 3: search_books(input('Type the name of a book...'), library)
        elif choice == 4:
            print(f"\nYou have a total of {len(book_dic(library))} books.\n")
            main_menu(library)
        elif choice == 5: highest_rated(library)
        elif choice == 6: longest_read(library)
        elif choice == 7: favorite_author(library)
        else:
            print('Exiting Library')
            pass


if __name__ == '__main__':
    main_menu("library.txt")
