### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = [
    'J.R.R. Tolkien',
    'Dan Brown',
    'William Shakespeare',
    'C.S. Lewis',
    'Jeff Smith',
    'Arthur Conan Doyle',
    'Edgar Allan Poe',
    'Stephen King']

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append('Mary Stewart')
print(my_authors)

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove('Jeff Smith')
print(my_authors)

my_authors.pop()
print(my_authors)
# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
print(my_authors[3])

# Now slice the list.

# Code here
# Example: my_authors[1:4]
print(my_authors[2:5])

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
author_tuple = (
    'J.R.R. Tolkien',
    'Dan Brown',
    'William Shakespeare',
    'C.S. Lewis',
    'Jeff Smith',
    'Arthur Conan Doyle',
    'Edgar Allan Poe',
    'Stephen King')

print(author_tuple[1:4])
print(author_tuple[0])
### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
author_set = {
    'J.R.R. Tolkien',
    'Dan Brown',
    'William Shakespeare',
    'C.S. Lewis',
    'Jeff Smith',
    'Arthur Conan Doyle',
    'Edgar Allan Poe',
    'Stephen King'}
print(author_set)
# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
author_set.add('Charles Dickens')
print(author_set)
# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
author_set.add('Edgar Allan Poe')
print(author_set)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)
for author in my_authors:
    print(author)

# for book in my_authors_tuple:
    # print(book)
for author in author_tuple:
    print(author)

# for book in my_authors_set:
    # print(book)

for author in author_set:
    print(author)


Bone = {"title": "Bone", "author": "Jeff Smith", "rating": 8.8}
print(Bone['author'])
Bone['publication'] = 2004
print(Bone)
Bone['rating'] = 9.6
print(Bone)
del Bone['publication']
print(Bone)

for key in Bone:
    print(key, Bone[key])

print(Bone.get('rating'))
print(Bone.get('pages', 'Key does not exist'))


