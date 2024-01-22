my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book2 = {
    "title": "The Davinci Code",
    "author": "Dan Brown",
    "year": 2003,
    "rating": 4.5,
    "pages": 689
}

my_book3 = {
    "title": "Shattered Seas",
    "author": "Byron Leavitt",
    "year": 2020,
    "rating": 4.6,
    "pages": 276
}

my_book4 = {
    "title": "Angels & Demons",
    "author": "Dan Brown",
    "year": 2000,
    "rating": 4.8,
    "pages": 768
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_summary(dic):
    title = dic['title']
    author = dic['author']
    year = dic['year']
    rating = dic['rating']
    pages = dic['pages']
    summary = f'{title} is written by {author} and came out in {year}. It has a {rating} rating, and is {pages} pages long.'
    return summary

print(book_summary(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(dic):
    title = dic['title']
    return title

def book_author(dic):
    author = dic['author']
    return author
def book_year(dic):
    year = dic['year']
    return year
def book_rating(dic):
    rating = dic['rating']
    return rating
def book_pages(dic):
    pages = dic['pages']
    return pages

print(book_title(my_book))
print(book_author(my_book))
print(book_year(my_book))
print(book_rating(my_book))
print(book_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def highest_rated(*args):
    highest = 0
    novel = ''
    for books in args:
        if books['rating'] > highest:
            highest = books['rating']
            novel = books['title']
        else:
            continue
    return novel

print(highest_rated(my_book, my_book2, my_book3, my_book4))

def longest_read(*args):
    longest = 0
    novel = ''
    for books in args:
        if books['pages'] > longest:
            longest = books['pages']
            novel = books['title']
    return novel

print(longest_read(my_book, my_book2, my_book3, my_book4))

def favorite_author(*args):

    author_dic = {}
    for book in args:
        author_name = book['author']
        if book['author'] in author_dic:
            author_dic[author_name] += 1
        else:
            author_dic[author_name] = 1
    return max(author_dic.items(), key=lambda x:x[1])[0]

print(favorite_author(my_book, my_book2, my_book3, my_book4))
