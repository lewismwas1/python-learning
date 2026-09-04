books = [
    {
        "title": "Python basics",
        "author": "John Smith",
        "year": 2024
    },
    {
        "title": "Java",
        "author": "Jane Doe",
        "year": 2018
    },
    {
        "title": "Python Crashcourse",
        "author": "Emily Davis",
        "year": 2020
    },
    {
        "title": "Css",
        "author": "Mike Johnson",
        "year": 2015
    }
]
for book in books:
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")

#searching for a book by title in the dictionary
search = input("Enter the book title you want to search for: ")
found = False
for book in books:
    if book['title'].lower() == search.lower():
        print(f"Book found: {book['title']} by {book['author']}, published in {book['year']}")
        found = True

if not found:
    print("Book not found.")

search = input("\nEnter the book title you want to search for: ")
found = False
for book in books:
    if search.lower() in book['title'].lower():
        print(f"Book found:{book['title']} by {book['author']}, published in {book['year']}")
        found = True

if not found:
    print("Book not found.")

#adding a new book to the dictionary
new_book = {
    "title": input("\nEnter the new book title: "),
    "author": input("Enter the new book author: "),
    "year": int(input("Enter the new book year of publication: "))    
}

#Checks if the book already exists in the library before adding it 
found = False
for book in books:
    if new_book['title'].lower() == book['title'].lower():
        print("Book already exists in the library.")
        found = True

if not found:
    books.append(new_book)
    print("Book added successfully.")